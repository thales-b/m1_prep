class Node:
    def __init__(self, value, left, right, rank=-1):
        self.value = value
        self.left = left
        self.right = right
        self.rank = rank

def join(left: Node, value, right: Node) -> Node:
    if left.rank >= right.rank:
        return Node(value, left, right, 1 + right.rank)
    return Node(value, right, left, 1 + left.rank)

def merge(h1: Node, h2: Node):
    if h1.value >= h2.value:
        join(h2.left, h2.value, merge(h2.right, h1))
    else:
        join(h1.left, h1.value, merge(h1.right, h2))