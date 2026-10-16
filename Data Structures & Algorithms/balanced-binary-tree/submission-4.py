# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        balanced = True

        def findHeight(root):
            nonlocal balanced
            if not root: return 0

            leftHeight = findHeight(root.left)
            rightHeight = findHeight(root.right)

            if abs(leftHeight - rightHeight) > 1:
                balanced = False

            return 1+ max(leftHeight, rightHeight)
        
        findHeight(root)
        return balanced