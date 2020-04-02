class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def cut(root, cout):
            if root is None:
                return None, cout
            if (root.left is None) & (root.right is None):
                if root.val == target:
                    return None, cout + 1
                else:
                    return root, cout
            else:
                root.left, cout = cut(root.left, cout)
                root.right, cout = cut(root.right, cout)
                return root, cout

        root, delete = cut(root, 0)
        while delete > 0:
            root, delete = cut(root, 0)
        return root