from sklearn.feature_extraction.text import TfidfVectorizer


def search(chunks, query, n=3):
    texts = [c["text"] for c in chunks]
    vec = TfidfVectorizer()
    mat = vec.fit_transform(texts)
    qvec = vec.transform([query])
    scores = (mat * qvec.T).toarray()
    order = sorted(range(len(chunks)), key=lambda i: scores[i][0], reverse=True)
    hits = []
    for i in order[:n]:
        hits.append((chunks[i], float(scores[i][0])))
    return hits
