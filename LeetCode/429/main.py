queue = []
if root is None:
    return []
queue.append(root)
result = []
while queue:
    level = []
    for _ in range(len(queue)):
        node = queue.pop(0)
        level.append(node.val)
        queue.extend(node.children)
    result.append(level)

return result