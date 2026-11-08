import heapq

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}

weights = {
    ("A", "B"): 1,
    ("A", "C"): 2,
    ("B", "D"): 2,
    ("B", "E"): 1,
    ("C", "F"): 3,
    ("C", "G"): 10,
    ("E", "G"): 1,
}


def ucs(start, goal):
    heap = [(0, start)]
    best = {start: 0}
    parent = {}
    order = []
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > best[node]:
            continue
        order.append(node)
        if node == goal:
            break
        for nxt in graph[node]:
            new_cost = cost + weights[(node, nxt)]
            if nxt not in best or new_cost < best[nxt]:
                best[nxt] = new_cost
                parent[nxt] = node
                heapq.heappush(heap, (new_cost, nxt))
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return order, path, best[goal]


def bfs_path(start, goal):
    queue = [start]
    seen = [start]
    parent = {}
    while queue:
        node = queue.pop(0)
        if node == goal:
            break
        for nxt in graph[node]:
            if nxt not in seen:
                seen.append(nxt)
                parent[nxt] = node
                queue.append(nxt)
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


order, path, cost = ucs("A", "G")
print("UCS processing order:", order)
print("UCS path:", path)
print("UCS cost:", cost)

total = 0
for i in range(len(path) - 1):
    total = total + weights[(path[i], path[i + 1])]
print("cost checked again by adding edges:", total)

short = bfs_path("A", "G")
short_cost = 0
for i in range(len(short) - 1):
    short_cost = short_cost + weights[(short[i], short[i + 1])]
print("BFS path on the same graph:", short)
print("BFS path cost:", short_cost)
print("BFS has fewer hops but costs more, because the C to G edge is expensive.")
