# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        result = []

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr is None: 
                    result.append("n")
                else:
                    result.append(str(curr.val))
                    queue.append(curr.left)
                    queue.append(curr.right)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "n":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1 # because we already checked the first element, now we are at 2nd
        while queue:
            curr = queue.popleft()
            if vals[i] != "n":
                curr.left = TreeNode(int(vals[i]))
                queue.append(curr.left)
            i += 1 # move i forward as we already added 1 element
            if vals[i] != "n":
                curr.right = TreeNode(int(vals[i]))
                queue.append(curr.right)
            i += 1
        return root
