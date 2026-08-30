class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        if beginWord == endWord: return 0
        if len(beginWord) == 1: return 2
        

        m = len(beginWord)
        graph = defaultdict(set)
        

        # Create the graph
        for word in wordList:
            for i in range(m):
                key = word[:i] + "*" + word[i+1:]
                if key not in graph:
                    graph[key] = {word}
                else:
                    graph[key].add(word)
        
        queue = deque([(beginWord, 0)])
        visited = set(beginWord)

        while queue:
            curr, dist = queue.popleft()
            if curr == endWord:
                return dist + 1
            for i in range(m):
                key = curr[:i] + "*" + curr[i+1:]
                for nbr in graph[key]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append((nbr, dist+1))
        
        return 0