# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return None
        maxSum = float('-inf')

        def helper(root):
            nonlocal maxSum
            if not root: return 0

            leftSum = max(helper(root.left),0)
            rightSum = max(helper(root.right),0)

            maxSum = max(maxSum, root.val + leftSum + rightSum)

            return root.val + max(leftSum, rightSum)
        
        helper(root)
        return maxSum

