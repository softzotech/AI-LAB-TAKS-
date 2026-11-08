import csv
import json
import time

from lab6_search import search
from task2_chunks import windows, pack

docs = json.load(open("corpus.json"))
queries = json.load(open("queries.json"))


def make_chunks(strategy):
    chunks = []
    for name, text in docs.items():
        words = text.split()
        if strategy == "overlap0":
            groups = windows(words, 40, 0)
            step = 40
        elif strategy == "overlap10":
            groups = windows(words, 40, 10)
            step = 30
        else:
            groups = pack(text, 40)
            step = 0
        start = 0
        for i, g in enumerate(groups):
            chunks.append({"id": strategy + "_" + name + "_" + str(i), "doc": name, "text": " ".join(g), "start": start, "end": start + len(g)})
            if step > 0:
                start = start + step
            else:
                start = start + len(g)
    return chunks


def tfidf_top(chunks, query):
    return search(chunks, query, 3)


model = None
try:
    from sentence_transformers import SentenceTransformer
    t0 = time.time()
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("model load time:", round(time.time() - t0, 1), "seconds")
except Exception as e:
    print("embeddings not available:", e)


def embed_top(chunks, query, embs):
    qvec = model.encode([query], normalize_embeddings=True, show_progress_bar=False)[0]
    scores = []
    for i in range(len(chunks)):
        total = 0
        for j in range(len(qvec)):
            total = total + float(embs[i][j]) * float(qvec[j])
        scores.append(total)
    order = sorted(range(len(chunks)), key=lambda i: scores[i], reverse=True)
    hits = []
    for i in order[:3]:
        hits.append((chunks[i], scores[i]))
    return hits


results = {}
log = []
for strategy in ["overlap0", "overlap10", "sentence"]:
    chunks = make_chunks(strategy)
    print(strategy, "chunks:", len(chunks))
    embs = None
    if model is not None:
        t0 = time.time()
        embs = model.encode([c["text"] for c in chunks], normalize_embeddings=True, show_progress_bar=False)
        print(strategy, "encode time:", round(time.time() - t0, 1), "seconds")
    for method in ["tfidf", "embedding"]:
        if method == "embedding" and model is None:
            continue
        scores = {}
        for split in ["dev", "test"]:
            hit_count = 0
            rr_total = 0
            total = 0
            for q in queries:
                if q["split"] != split or q["doc"] is None:
                    continue
                total = total + 1
                if method == "tfidf":
                    top = tfidf_top(chunks, q["query"])
                else:
                    top = embed_top(chunks, q["query"], embs)
                ev = q["evidence"].replace(".", "")
                rank = 0
                for i, (c, s) in enumerate(top):
                    if ev in c["text"].replace(".", ""):
                        rank = i + 1
                        break
                if rank > 0:
                    hit_count = hit_count + 1
                    rr_total = rr_total + 1.0 / rank
                row = [strategy, method, split, q["query"]]
                for c, s in top:
                    row.append(c["id"])
                    row.append(round(s, 3))
                row.append(rank)
                log.append(row)
            scores[split] = (round(hit_count / total, 3), round(rr_total / total, 3))
        results[(strategy, method)] = scores
        print(strategy, method, "dev Hit@3/MRR@3:", scores["dev"], "test Hit@3/MRR@3:", scores["test"])

with open("retrieval_log.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["strategy", "method", "split", "query", "top1", "score1", "top2", "score2", "top3", "score3", "rank"])
    for row in log:
        w.writerow(row)

best = None
best_score = -1
for key, scores in results.items():
    value = scores["dev"][0] + scores["dev"][1]
    if value > best_score:
        best_score = value
        best = key
print("picked setup:", best, "dev:", results[best]["dev"], "held out test:", results[best]["test"])

print("unanswerable queries still get text back, but no answer is asserted:")
for q in queries:
    if q["doc"] is None:
        chunks = make_chunks(best[0])
        top = tfidf_top(chunks, q["query"])
        print(q["query"], "->", top[0][0]["id"], "but this is only the closest text, not an answer")
