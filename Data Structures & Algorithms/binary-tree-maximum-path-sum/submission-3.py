# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node: return 0

            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)
            
            maxSum = max(maxSum, leftSum + rightSum + node.val)

            return max(leftSum+node.val, rightSum+node.val)
        
        dfs(root)
        return maxSum