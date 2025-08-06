# Trees are made of nodes, with each node having a left and/or right child
# The node at the top of the tree with no incoming edges is the root node
# The nodes at the bottom of the tree are leaf nodes
# The node in the middle are branch nodes

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data