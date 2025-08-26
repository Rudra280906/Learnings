# My Solution to Binary Tree Level Order Traversal Problem from Leetcode
from collections import deque
def levelOrder(root):
    order = []
    if not root:
        return []
    queue = deque([(root, 0)])
    while queue:
        item = queue.popleft()
        node = item[0]
        level = item[1]
        try:
            order[level].append(node.val)
        except:
            order.append([node.val])
        finally:
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
    return order