# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        diam = 0
        def maxDepth(root):
            nonlocal diam
            if not root: return 0

            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)

            diam = max(diam, leftDepth+rightDepth)

            return 1 + max(leftDepth,rightDepth)
        maxDepth(root)
        return diam
