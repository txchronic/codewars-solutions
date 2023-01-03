class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: Node) -> None | list:
    res, q = [], [node]

    while q:
        n = q.pop(0)

        if n:
            res.append(n.value)
            q += [n.left, n.right]

    return res if node else []
