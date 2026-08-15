"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Sprinklr
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        node_map = {}
        queue = deque([node])
        visited = {node}

        while queue:
            curr = queue.popleft()
            new_node = Node(val = curr.val)
            node_map[curr] = new_node

            for nbr in curr.neighbors:
                if nbr not in visited:
                    queue.append(nbr)
                    visited.add(nbr)
        
        for existing_node in node_map:
            node_copy = node_map[existing_node]
            for nbr in existing_node.neighbors:
                node_copy.neighbors.append(node_map[nbr])
        
        return node_map[node]