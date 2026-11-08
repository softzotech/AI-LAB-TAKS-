from sklearn.feature_extraction.text import TfidfVectorizer

questions = [
    "When does the library open?",
    "How do I apply for the hostel?",
    "Where can I see the exam schedule?",
    "How do I get my transcript?",
    "What is the fee deadline?",
]

answers = [
    "The library opens at 8 in the morning and closes at 10 at night.",
    "Fill the hostel form at the admin office and attach your fee receipt.",
    "The exam schedule is on the notice board and the student portal.",
    "Apply at the exam office with your student card and a copy of your CNIC.",
    "The fee deadline is the 10th of every month.",
]

vec = TfidfVectorizer()
mat = vec.fit_transform(questions)


def reply(query):
    query = query.strip()
    if query == "":
        return "Please type a question."
    for i, q in enumerate(questions):
        if query.lower() == q.lower():
            return answers[i]
    qvec = vec.transform([query])
    scores = (mat * qvec.T).toarray()
    best = 0
    best_score = scores[0][0]
    for i in range(1, len(questions)):
        if scores[i][0] > best_score:
            best_score = scores[i][0]
            best = i
    if best_score >= 0.35:
        return "Did you mean: " + questions[best] + " " + answers[best]
    return "Sorry, I do not know the answer to that."


if __name__ == "__main__":
    print("Ask a question, or type bye to stop.")
    while True:
        try:
            query = input("you: ")
        except EOFError:
            break
        if query.strip().lower() == "bye":
            break
        print("bot:", reply(query))
