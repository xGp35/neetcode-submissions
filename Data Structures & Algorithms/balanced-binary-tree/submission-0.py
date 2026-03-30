# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        self.balanced = True

        def height_check(node):
            if not node: return 0

            leftHeight = height_check(node.left)
            rightHeight = height_check(node.right)

            if abs(leftHeight - rightHeight) > 1:
                self.balanced = False

            return 1 + max(leftHeight, rightHeight)
        
        height_check(root)

        return self.balanced