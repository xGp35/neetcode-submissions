class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTrie = Trie()
        for word in words:
            myTrie.add(word)
        
        m, n = len(board), len(board[0])

        res, visited = set(), set()

        def dfs(row, col, node, curWord):
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            if board[row][col] == '*':
                return
            ch = board[row][col]
            if ch not in node.children:
                return

            board[row][col] = '*'
            actual_node_obj = node.children[ch]
            curWord += ch

            if actual_node_obj.endOfWord:
                res.add(curWord)

            neighbors = [(row+1,col),(row,col+1),(row-1,col),(row,col-1)]

            for nbr in neighbors:
                r,c = nbr
                dfs(r,c, actual_node_obj, curWord)

            board[row][col] = ch

        for row in range(m):
            for col in range(n):
                dfs(row, col, myTrie.root, "")
        
        return list(res)

        