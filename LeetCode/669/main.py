# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def cut(root):
            if root is None:
                return None

            if root.val > R:
                # root.right = None
                root = cut(root.left)
                return root
            elif root.val < L:
                # root.left = None
                root = cut(root.right)
                return root
            else:
                root.left = cut(root.left)
                root.right = cut(root.right)
                return root

        return cut(root)
