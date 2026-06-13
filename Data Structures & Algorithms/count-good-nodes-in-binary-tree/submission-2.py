# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        def dfs(node, max_in_branch):

            adder = 1 if node.val >= max_in_branch else 0
            max_in_branch = max(node.val, max_in_branch)

            if node.left:
                left_good = dfs(node.left, max_in_branch)
            else:
                left_good =  0
            if node.right:
                right_good = dfs(node.right, max_in_branch)
            else:
                right_good = 0

            return adder + left_good + right_good
        
        return dfs(root, root.val)
            
