import heapq

from lab4_astar import graph, h, search

print("first three expansions by hand:")
print("S: g 0 + h 5 = f 5")
print("A: g 1 + h 4 = f 5")
print("C: g 3 + h 2 = f 5")
print("next is G with f 6, which beats B with f 8")


def true_cost(start):
    heap = [(0, start)]
    best = {start: 0}
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > best[node]:
            continue
        if node == "G":
            return cost
        for nxt, w in graph[node]:
            new_cost = cost + w
            if nxt not in best or new_cost < best[nxt]:
                best[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))
    return None


print("node | h | true remaining cost | admissible")
for node in ["S", "A", "C", "B", "G"]:
    real = true_cost(node)
    ok = "yes"
    if h[node] > real:
        ok = "no"
    print(node, "|", h[node], "|", real, "|", ok)

h2 = {"S": 5, "A": 4, "C": 10, "B": 4, "G": 0}
print("original h(C):", h["C"], "changed h(C):", h2["C"], "true cost from C:", true_cost("C"))
path, cost, order, expanded = search("S", "G", h2)
print("overestimate run path:", path)
print("overestimate run cost:", cost)
print("overestimate run processed:", order)
print("The path and the cost both changed, so the overestimate removed the guarantee.")
