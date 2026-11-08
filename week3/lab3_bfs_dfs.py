graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}


def bfs(start, goal):
    queue = [start]
    seen = [start]
    parent = {}
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
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
    return order, path


def dfs(start, goal):
    stack = [start]
    seen = [start]
    parent = {}
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node == goal:
            break
        for nxt in reversed(graph[node]):
            if nxt not in seen:
                seen.append(nxt)
                parent[nxt] = node
                stack.append(nxt)
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return order, path


order, path = bfs("A", "G")
print("BFS visit order:", order)
print("BFS path:", path)

order, path = dfs("A", "G")
print("DFS visit order:", order)
print("DFS path:", path)
