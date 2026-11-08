import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2), ("B", 3)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}

h = {"S": 5, "A": 4, "C": 2, "B": 4, "G": 0}


def search(start, goal, heur):
    heap = [(heur[start], 0, start, 0)]
    count = 1
    best = {start: 0}
    parent = {}
    order = []
    expanded = 0
    while heap:
        f, _, node, cost = heapq.heappop(heap)
        if cost > best[node]:
            continue
        order.append(node)
        if node == goal:
            break
        expanded = expanded + 1
        for nxt, w in graph[node]:
            new_cost = cost + w
            if nxt not in best or new_cost < best[nxt]:
                best[nxt] = new_cost
                parent[nxt] = node
                heapq.heappush(heap, (new_cost + heur[nxt], count, nxt, new_cost))
                count = count + 1
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path, best[goal], order, expanded


if __name__ == "__main__":
    path, cost, order, expanded = search("S", "G", h)
    print("A* path:", path)
    print("A* cost:", cost)
    print("A* processed:", order)
    print("A* expanded:", expanded)

    zero = {"S": 0, "A": 0, "C": 0, "B": 0, "G": 0}
    path, cost, order, expanded = search("S", "G", zero)
    print("UCS path:", path)
    print("UCS cost:", cost)
    print("UCS processed:", order)
    print("UCS expanded:", expanded)
