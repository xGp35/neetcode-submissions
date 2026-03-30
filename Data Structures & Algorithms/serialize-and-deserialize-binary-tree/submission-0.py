# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        dq = deque([root])

        while dq:
            curr = dq.popleft()
            
            if curr:
                result.append(str(curr.val))
                dq.append(curr.left)
                dq.append(curr.right)
            else: 
                result.append('null')

        return '#'.join(result)
              
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split('#')

        level = [None if elem == 'null' else int(elem) for elem in arr]

        if not level or level[0] is None:
            return None

        root = TreeNode(level[0])
        queue = deque([root])
        i = 1

        while queue and i < len(level):
            node = queue.popleft()

            # Left child
            if i < len(level) and level[i] is not None:
                node.left = TreeNode(level[i])
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(level) and level[i] is not None:
                node.right = TreeNode(level[i])
                queue.append(node.right)
            i += 1

        return root


