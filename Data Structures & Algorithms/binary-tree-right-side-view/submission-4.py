# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = deque([root])
        result = []

        while queue:
            width = len(queue)
            for i in range(width):
                curr = queue.popleft()
                if i == width-1: result.append(curr.val)
                
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        return result