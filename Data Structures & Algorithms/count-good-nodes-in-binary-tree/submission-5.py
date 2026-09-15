# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        def helper(root, maxSoFar):
            if not root: return 0

            ans = 0
            if root.val >= maxSoFar:
                maxSoFar = root.val
                ans = 1
            
            leftCount = helper(root.left, maxSoFar)
            rightCount = helper(root.right, maxSoFar)

            return (ans + leftCount + rightCount)
        
        return helper(root, float('-inf'))