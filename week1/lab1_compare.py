def rule_decision(score, doc, attend, fee):
    if score >= 70 and doc and attend >= 75 and fee:
        return "Approve"
    return "Hold"


def simple_decision(score):
    if score >= 70:
        return "Approve"
    return "Hold"


students = [
    ["Ali", 82, True, 90, True],
    ["Sara", 85, True, 60, True],
    ["Usman", 68, True, 80, True],
    ["Ayesha", 91, False, 85, True],
    ["Bilal", 70, True, 75, True],
]

print("name | rule method | score only method | same")
for s in students:
    first = rule_decision(s[1], s[2], s[3], s[4])
    second = simple_decision(s[1])
    same = "agree"
    if first != second:
        same = "disagree"
    print(s[0], "|", first, "|", second, "|", same)

print("The rule method looks at four things, the score method looks at one.")
print("That is why they disagree when a student passes the score but fails another condition.")
print("A conversational test is similar: it only checks fluent replies, not real understanding.")
