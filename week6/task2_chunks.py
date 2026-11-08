import json


def windows(words, size, overlap):
    if overlap < 0 or overlap >= size:
        print("bad overlap")
        return []
    chunks = []
    step = size - overlap
    start = 0
    while start < len(words):
        chunks.append(words[start:start + size])
        if start + size >= len(words):
            break
        start = start + step
    return chunks


def sentences(text):
    parts = text.split(". ")
    out = []
    for p in parts:
        p = p.strip()
        if p:
            out.append(p)
    return out


def pack(text, budget):
    chunks = []
    current = []
    for s in sentences(text):
        words = s.split()
        if len(words) > budget:
            if current:
                chunks.append(current)
                current = []
            i = 0
            while i < len(words):
                chunks.append(words[i:i + budget])
                i = i + budget
            continue
        if len(current) + len(words) > budget:
            chunks.append(current)
            current = words
        else:
            current = current + words
    if current:
        chunks.append(current)
    return chunks


if __name__ == "__main__":
    docs = json.load(open("corpus.json"))
    for name, text in docs.items():
        words = text.split()
        w0 = windows(words, 40, 0)
        w10 = windows(words, 40, 10)
        s = pack(text, 40)
        print(name, "words:", len(words), "overlap0:", len(w0), "overlap10:", len(w10), "sentence:", len(s))
        repeated = 0
        for c in w10:
            repeated = repeated + len(c)
        print(name, "repeated words in overlap10:", repeated - len(words))
        if name == "late":
            evidence = "Illness extensions require medical evidence before the deadline"
            for label, group in [["overlap0", w0], ["overlap10", w10], ["sentence", s]]:
                found = "no"
                for c in group:
                    if evidence in " ".join(c):
                        found = "yes"
                print("late", label, "evidence in one chunk:", found)

    print("empty text:", windows([], 40, 0), pack("", 40))
    print("short text:", windows("hello world".split(), 40, 0), pack("hello world", 40))
    print("bad overlap:", windows("a b c".split(), 40, 40))
    long = " ".join(["word"] * 95) + "."
    print("long sentence chunks:", len(pack(long, 40)))
