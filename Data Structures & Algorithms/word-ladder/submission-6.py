class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        graph = defaultdict(list)
        wordList.append(beginWord) # Just adding the beginWord to the wordlist as all other words are in this list except the beginWord.

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                graph[pattern].append(word)

        visited = set(beginWord)
        queue = deque([beginWord])

        count = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return count

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nbr in graph[pattern]:
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append(nbr)
            count += 1
        
        return 0