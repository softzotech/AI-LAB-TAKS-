from lab2_model import Controller

c = Controller()

tests = [
    [30, 2],
    [30, 2],
    [27, 2],
    [22, 2],
    [22, 2],
    [19, 1],
    [19, 1],
    [25, 0],
    [25, 0],
    [30, 1],
]

print("before | temperature | people | target | send command")
for t in tests:
    before = c.last
    mode, send = c.decide(t[0], t[1])
    print(before, "|", t[0], "|", t[1], "|", mode, "|", send)
