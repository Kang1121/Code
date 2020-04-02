class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # s = 0
        def sum(root, s):
            if not root:
                return 0
            s = s * 10 + root.val
            if (not root.left) & (not root.right):
                return s
            else:
                return sum(root.left, s) + sum(root.right, s)

        return sum(root, 0)