# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check = True

        def maxDepth(curr):
            if not curr: return 0

            leftDepth = maxDepth(curr.left)
            rightDepth = maxDepth(curr.right)

            if abs(rightDepth-leftDepth) > 1:
                self.check = False

            return 1 + max(leftDepth, rightDepth)

        maxDepth(root)
        return self.check