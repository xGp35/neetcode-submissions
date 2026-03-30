# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # There is a pretty easy O(n) space complexity solution to this.
        # We can just store elements in an array till we reach kth node

        # But Neetcode said we should try O(1) space complexity solution
        # So, we keep track of how many nodes are visited in order
        # Once we reach k elements visited, we return the node.

        stack = []
        counter = 0
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            counter += 1
            if counter == k:
                return current.val
            current = current.right
        
        return 

            
