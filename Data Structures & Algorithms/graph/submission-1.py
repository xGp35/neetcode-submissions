class GraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# First do adjacency list solution then do GraphNode based.

class Graph:
    
    def __init__(self):
        self.nodes = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.nodes:
            src_node = GraphNode(src)
            self.nodes[src] = src_node
        if dst not in self.nodes:
            dst_node = GraphNode(dst)
            self.nodes[dst] = dst_node
        self.nodes[src].neighbors.append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.nodes:
            return False
        if dst not in self.nodes[src].neighbors:
            return False
        else:
            self.nodes[src].neighbors.remove(dst)
            return True
            

    def hasPath(self, src: int, dst: int) -> bool:
        stack = [self.nodes[src]]
        visited = {src}

        while stack:
            curr = stack.pop()
            if curr.val == dst:
                return True
            for nbr in curr.neighbors:
                if nbr not in visited:
                    stack.append(self.nodes[nbr])
                    visited.add(nbr)
        return False
