graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}


def dls(node, goal, limit, path):
    if node == goal:
        return path
    if limit == 0:
        return "CUTOFF"
    hit_cutoff = False
    for nxt in graph[node]:
        if nxt in path:
            continue
        result = dls(nxt, goal, limit - 1, path + [nxt])
        if result == "CUTOFF":
            hit_cutoff = True
        elif result != "FAILURE":
            return result
    if hit_cutoff:
        return "CUTOFF"
    return "FAILURE"


def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(start, goal, depth, [start])
        if result != "CUTOFF":
            return result
    return "CUTOFF"


print("DLS:")
for limit in [1, 2, 3, 4]:
    result = dls("A", "G", limit, ["A"])
    if isinstance(result, list):
        print("limit", limit, "FOUND", result)
    else:
        print("limit", limit, result)

print("IDDFS:")
for max_depth in [1, 2, 3, 4]:
    result = iddfs("A", "G", max_depth)
    if isinstance(result, list):
        print("max depth", max_depth, "FOUND", result)
    else:
        print("max depth", max_depth, result)
