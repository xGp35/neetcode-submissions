# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        def helper(curr, curSum):
            if not curr: return False
            if not curr.left and not curr.right and curSum + curr.val == targetSum:
                return True

            if curr.left and helper(curr.left, curSum + curr.val):
                return True
            if curr.right and helper(curr.right, curSum + curr.val):
                return True

            return False
        
        return helper(root, 0)
