# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        hash_map = {val:i for i, val in enumerate(inorder)}

        self.gpi = 0
        def dfs(l,r):
            if l > r: return None

            root_val = preorder[self.gpi]
            self.gpi += 1
            root = TreeNode(root_val)
            mid = hash_map[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)

            return root
        
        return dfs(0, len(preorder)-1)