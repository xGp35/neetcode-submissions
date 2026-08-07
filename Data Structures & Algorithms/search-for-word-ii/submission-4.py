class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        result = set()

        # Create a Trie
        WS2Trie = Trie()
        for word in words:
            WS2Trie.add(word)

        def dfs(node, nodeT, curWord):
            row, col = node
            ch = board[row][col]

            if ch not in nodeT.children:
                return

            nodeT = nodeT.children[ch]
            curWord = curWord + ch

            if nodeT.endOfWord:
                result.add(curWord)
            
            board[row][col] = '#'
            neighbors = [(row+1, col),(row, col+1),(row-1,col),(row,col-1)]

            for nbr in neighbors:
                r, c = nbr
                if(
                    0 <= r < m and
                    0 <= c < n and
                    board[r][c] != '#'
                ):
                    dfs(nbr, nodeT, curWord)

            board[row][col] = ch
        
        for row in range(m):
            for col in range(n):
                if board[row][col] in WS2Trie.root.children:
                    dfs((row, col), WS2Trie.root, "")
                
        return list(result)
        
