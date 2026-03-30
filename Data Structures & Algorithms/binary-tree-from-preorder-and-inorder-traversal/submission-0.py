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
        
        # Map value -> index for inorder Traversal
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        preorder_index = 0

        def helper(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            
            # Pick current root from preorder
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)

            # Build left & right subtrees
            index = inorder_index[root_val]
            root.left = helper(left, index -1)
            root.right = helper(index + 1, right)

            return root
        
        return helper (0, len(inorder)-1)
