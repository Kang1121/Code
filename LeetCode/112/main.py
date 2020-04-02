class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def search(root, value):
            if not root:
                return False
            if (root.left is None) & (root.right is None):
                if (root.val + value) == sum:
                    return True
                else:
                    return False
            else:
                return search(root.left, root.val + value) | search(root.right, root.val + value)
        return search(root, 0)