#My solution for Validate Binary Search Tree Problem on Leetcode
def isValidBST(root) -> bool:
    running_list = []
    def DFS(root):
        if not root:
            return None
        else:
            DFS(root.left)
            running_list.append(root.val)
            DFS(root.right)
    DFS(root)
    print(running_list)
    if running_list != sorted(list(set(running_list))):
        return False
    else:
        return True