# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        def inorder(root):
            if not root: return 

            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:
                return False
        
        return True

