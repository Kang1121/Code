class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root):
    white, gray = 0, 1
    stack = [(white, root)]
    res = []
    while stack:
        color, node = stack.pop()
        if node is None:
            continue
        if color == 0:
            stack.append((white, node.right))
            stack.append((gray, node))
            stack.append((white, node.left))
        else:
            res.append(node.val)

    return res


def create(list, root, i):
    if i >= len(list):
        return None
    if list[i] is None:
        return None
    else:
        root = TreeNode(list[i])
        root.left = create(list, root.left, 2 * i + 1)
        root.right = create(list, root.right, 2 * i + 2)
        return root


l1 = [1, None, 2, None, None, 3]
root = TreeNode(l1[0])
l = create(l1, root, 0)
# print(root)
# while root.val is not None:
#     print(root.val)
#     root

h = inorderTraversal(l)
print(h)