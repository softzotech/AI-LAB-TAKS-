tree = [[[3, 5], [2, 9]], [[6, 8], [0, 1]]]

leaves = [0]


def minimax(node, is_max):
    if isinstance(node, int):
        leaves[0] = leaves[0] + 1
        return node
    if is_max:
        best = -1000
        for child in node:
            value = minimax(child, False)
            if value > best:
                best = value
        return best
    best = 1000
    for child in node:
        value = minimax(child, True)
        if value < best:
            best = value
    return best


def alphabeta(node, is_max, alpha, beta):
    if isinstance(node, int):
        leaves[0] = leaves[0] + 1
        return node
    if is_max:
        best = -1000
        for child in node:
            value = alphabeta(child, False, alpha, beta)
            if value > best:
                best = value
            if best > alpha:
                alpha = best
            if alpha >= beta:
                break
        return best
    best = 1000
    for child in node:
        value = alphabeta(child, True, alpha, beta)
        if value < best:
            best = value
        if best < beta:
            beta = best
        if beta <= alpha:
            break
    return best


leaves[0] = 0
print("minimax value:", minimax(tree, True))
print("minimax leaves checked:", leaves[0])

leaves[0] = 0
print("alpha-beta value:", alphabeta(tree, True, -1000, 1000))
print("alpha-beta leaves checked:", leaves[0])

tree2 = [[[3, 5], [2, 9]], [[0, 1], [6, 8]]]

leaves[0] = 0
print("reordered minimax value:", minimax(tree2, True))
print("reordered minimax leaves checked:", leaves[0])

leaves[0] = 0
print("reordered alpha-beta value:", alphabeta(tree2, True, -1000, 1000))
print("reordered alpha-beta leaves checked:", leaves[0])
print("The value stayed 5, but the reordered tree let alpha-beta skip two leaves.")
