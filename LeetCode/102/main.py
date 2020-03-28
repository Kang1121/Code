
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        queue.append(root)
        result = []
        if root == None:
            return result
        while queue:
            res = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node == None:
                    continue
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if res:
                result.append(res)
        return result