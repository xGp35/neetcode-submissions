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
            myTrie.add(word) # Constructing the Trie. Trie construction is complete.
        
        m, n = len(board), len(board[0]) 

        res, visited = set(), set()

        # dfs to traverse the trie starting from (row,col). node is the Trie node
        # So basically keeping track of both the TrieNode and the (row,col) I am currently at.
        def dfs(row, col, node, curWord):
            if not (0<=row<m and 0<=col<n and (row,col) not in visited and board[row][col] in node.children): # If the current (row,col) is invalid or visited, return. Also return, if value at this (row,col), ie. board[row][col], is not one of the doors of TrieNode you are at.
                return
            
            
            visited.add((row, col))

            actual_node_obj = node.children[board[row][col]] # this is the actual value, we are going into. for example, if node was Trie.root and we are at "b" of "back". b is one of the children of root. So, we ahve to do dfs on all nbrs of (row,col). For those, the Trie node to be used would be the room of b. That room of b is node.children[board[row][col]], here board[row][col] = b. and we are going into that.
            curWord += board[row][col] 

            if actual_node_obj.endOfWord:
                res.add(curWord) #If b was last letter of any word, we add it to result.

            # Complete normal DFS + backtrack start
            neighbors = [(row+1,col),(row,col+1),(row-1,col),(row,col-1)]

            for nbr in neighbors:
                r,c = nbr
                dfs(r,c, actual_node_obj, curWord)

            visited.remove((row,col))
            # Complete normal DFS + backtrack end

        for row in range(m):
            for col in range(n):
                dfs(row, col, myTrie.root, "")
        
        return list(res)

        