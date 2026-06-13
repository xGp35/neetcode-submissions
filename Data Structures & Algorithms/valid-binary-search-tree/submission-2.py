# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # just do a inorder traversal, it should be in sorted order
        if not root: return True
        def dfs(node, res):
            if not node: return None

            dfs(node.left, res)
            res.append(node.val)
            dfs(node.right, res)
            return res
        
        res = []
        dfs(root,res)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True
            