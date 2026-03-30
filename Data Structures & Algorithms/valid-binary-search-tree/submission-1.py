# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False

        result = []
        def dfs(node):
            if not node: return None

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)   
        print(result)
        for i in range(len(result)-1):
            if result[i] >= result [i+1]:
                return False
        
        return True