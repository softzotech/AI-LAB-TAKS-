import json

from lab6_search import search
from task2_chunks import windows

docs = json.load(open("corpus.json"))

chunks = []
for name, text in docs.items():
    words = text.split()
    groups = windows(words, 40, 10)
    for i, g in enumerate(groups):
        chunks.append({"id": "overlap10_" + name + "_" + str(i), "doc": name, "text": " ".join(g), "start": i * 30, "end": i * 30 + len(g)})

model = None
embs = None
try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embs = model.encode([c["text"] for c in chunks], normalize_embeddings=True, show_progress_bar=False)
    print("using real embeddings")
except Exception as e:
    print("using tfidf only:", e)


def top3(query):
    if model is not None:
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
    return search(chunks, query, 3)


if __name__ == "__main__":
    print("Ask a question, or type bye to stop.")
    while True:
        try:
            query = input("you: ")
        except EOFError:
            break
        if query.strip().lower() == "bye":
            break
        if query.strip() == "":
            print("bot: please type a question")
            continue
        top = top3(query)
        for c, s in top:
            print(c["id"], "score", round(s, 3), "words", c["start"], "-", c["end"])
        try:
            ans = input("show the first passage? (yes/no) ")
        except EOFError:
            break
        if ans.strip().lower() == "yes":
            print(top[0][0]["text"])
