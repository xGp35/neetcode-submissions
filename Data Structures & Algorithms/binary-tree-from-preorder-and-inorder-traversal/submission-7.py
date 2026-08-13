# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_ord_map = {val: i for i, val in enumerate(inorder)}

        pre_ord_idx = 0
        left, right = 0, len(inorder) -1

        def in_ord_helper(left, right):
            nonlocal pre_ord_idx
            if left > right: return None
            
            
            # Get the root value from preorder at the current index,
            root_val = preorder[pre_ord_idx]
            root = TreeNode(root_val)
            
            pre_ord_idx += 1

            in_ord_idx = in_ord_map[root_val]

            root.left = in_ord_helper(left, in_ord_idx -1)
            root.right = in_ord_helper(in_ord_idx + 1, right)

            return root
        
        
        return in_ord_helper(left, right)