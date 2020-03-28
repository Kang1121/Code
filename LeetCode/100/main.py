class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def judge(root1, root2):
    if (root1 is not None) & (root2 is not None):
        if root1.val == root2.val:
            return judge(root1.left, root2.left) & judge(root1.right, root2.right)
        else:
            return False
    elif (root1 is None) & (root2 is None):
        return True
    else:
        return False


def create(list, i, root):
    if i >= len(list):
        return None
    if list[i] is None:
        return None
    else:
        root = TreeNode(list[i])
        root.left = create(list, 2 * i + 1, root.left)
        root.right = create(list, 2 * i + 2, root.right)
        return root


a = [1, None, 1]
b = [1, 1]
root = TreeNode(None)
roota = create(a, 0, root)
rootb = create(b, 0, root)
# print(type(roota))
# print(type(rootb))
print(judge(roota, rootb))


