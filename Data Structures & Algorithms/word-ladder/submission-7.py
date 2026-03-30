class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord): return 0
        m = len(beginWord)

        wordList.append(beginWord)
        graph = defaultdict(list)

        for word in wordList:
            for j in range(m):
                pattern = word[:j] + "*" + word[j+1:]
                graph[pattern].append(word)

        visited = {beginWord}
        queue = deque([beginWord])

        count = 1

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord: return count

                for j in range(m):
                    pattern = curr[:j] + "*" + curr[j+1:]
                    for nbr in graph[pattern]:
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append(nbr)
            count += 1
        return 0