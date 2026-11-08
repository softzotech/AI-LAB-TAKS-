def check(score, doc, attend, fee):
    if score >= 70 and doc and attend >= 75 and fee:
        return "Approve"
    return "Hold"


cases = [
    ["all pass", 82, True, 90, True, "Approve", "all four conditions pass"],
    ["low attendance", 85, True, 60, True, "Hold", "attendance below 75"],
    ["fee unpaid", 88, True, 80, False, "Hold", "fee not paid"],
    ["on the limit", 70, True, 75, True, "Approve", "score and attendance exactly on the limit"],
]

print("case | score | document | attendance | fee | expected | result | reason")
for c in cases:
    result = check(c[1], c[2], c[3], c[4])
    print(c[0], "|", c[1], "|", c[2], "|", c[3], "|", c[4], "|", c[5], "|", result, "|", c[6])
