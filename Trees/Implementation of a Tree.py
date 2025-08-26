# Trees are made of nodes, with each node having a left and/or right child
# The node at the top of the tree with no incoming edges is the root node
# The nodes at the bottom of the tree are leaf nodes
# The node in the middle are branch nodes
from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
# DFS Inorder (Left -> Root -> Right)
def inorder(root):
    if not root:
        return None
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
# DFS Preorder (Root -> Left -> Right)
def preorder(root):
    if not root:
        return None
    else:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
# DFS Postorder (Left  -> Right -> Root)
def postorder(root):
    if not root:
        return None
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
# BFS Queues (Uses 2 Queues, one for current, one for next level)
def bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(result)

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("G")
root.right.left = Node("F")

inorder(root)