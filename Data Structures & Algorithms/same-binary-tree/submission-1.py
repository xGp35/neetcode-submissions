# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list_p = []
        list_q = []

        def df_traversal(root,result):
            if not root:
                result.append(None)
                return None
            result.append(root.val)
            
            df_traversal(root.left, result)
            df_traversal(root.right, result)
            
            return None
        
        df_traversal(p,list_p)
        df_traversal(q, list_q)

        return list_p == list_q
