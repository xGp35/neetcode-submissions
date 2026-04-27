# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.diameter = 0

        def max_depth(node):
            if not node: return 0

            leftDepth = max_depth(node.left)
            rightDepth = max_depth(node.right)

            self.diameter = max(self.diameter, leftDepth+rightDepth)

            return 1 + max(leftDepth, rightDepth)

        max_depth(root)
        return self.diameter
