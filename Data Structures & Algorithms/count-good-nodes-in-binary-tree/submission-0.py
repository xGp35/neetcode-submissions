# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_in_branch):
            if not node: return 0
            adder = 0
            
            if node.val < max_in_branch: adder = 0
            else: adder = 1
            max_in_branch = max(node.val, max_in_branch)

            if node.left: left_val = dfs(node.left, max_in_branch)
            else: left_val = 0
            if node.right: right_val = dfs(node.right, max_in_branch)
            else: right_val = 0
            return adder + left_val + right_val
        
        goodCount = dfs(root, root.val)
        return goodCount
