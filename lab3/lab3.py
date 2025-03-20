class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: Node) -> Node:
    if tree is None:
        return None

    tree.left, tree.right = tree.right, tree.left

    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)

    return tree

def do_levels(root, level=0, levels=None):
    if root is None:
        return
    if levels is None:
        levels = []
    if len(levels) == level:
        levels.append([])
    levels[level].append(str(root.value))

    do_levels(root.left, level + 1, levels)
    do_levels(root.right, level + 1, levels)

    return levels

def print_tree(root):
    levels = do_levels(root)
    for level in levels:
        print(" ".join(level))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Оригінальне дерево:")
print_tree(root)

inverted_root = invert_binary_tree(root)

print("\nІнвертоване дерево:")
print_tree(inverted_root)
