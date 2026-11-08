import re

samples = [
    "AI, search!",
    "I can't log in.",
    "Email me at help@example.com please.",
    "CS4944 version 2.1 is out.",
    "",
    "میں یونیورسٹی جا رہا ہوں۔",
]

for text in samples:
    plain = text.split()
    words = re.findall(r"\w+", text)
    print("text:", text)
    print("whitespace tokens:", plain, len(plain))
    print("word tokens:", words, len(words))

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    for text in ["AI, search!", "I can't log in."]:
        print("model tokens:", model.tokenizer.tokenize(text))
except Exception as e:
    print("model tokenizer not available:", e)

print("The word pattern drops punctuation, so an email becomes three pieces.")
print("The whitespace split keeps punctuation attached to the words.")
print("Lowercasing everything can merge words that were meant to stay different.")
