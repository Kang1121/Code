

def exist(root):
    if root is None:
        return 0

    if root.val == 0:
        if exist(root.left) | exist(root.right) == 0:
            root = None
            return 0
    else:
        return 1

