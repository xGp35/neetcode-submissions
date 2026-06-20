class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create an adjacency list of pattern to words
        # make a wueue and start bfs with width tracking

        n = len(wordList)
        m = len(wordList[0])
        wordList.append(beginWord)

        nei = defaultdict(list)
        for word in wordList:
            for j in range(m):
                pattern = word[0:j] + '*' + word[j+1:]
                nei[pattern].append(word)
        # Now my adjacency list is ready

        queue = deque([beginWord])
        visited = set(beginWord)
        result = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return result
                for j in range(m):
                    pattern = word[0:j] + '*' + word[j+1:]
                    for nbr in nei[pattern]:
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append(nbr)
            result += 1

        return 0
