# class GraphNode:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# First do adjacency list solution then do GraphNode based.

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        else:
            return False

    def hasPath(self, src: int, dst: int) -> bool:
        stack = [src]
        visited = {src}

        while stack:
            curr = stack.pop()
            if curr == dst:
                return True
            for nbr in self.graph[curr]:
                if nbr not in visited:
                    stack.append(nbr)
                    visited.add(nbr)
        return False
