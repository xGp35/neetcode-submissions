class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        curSet = []

        def dfs(i):
            if i == len(s):
                result.append(curSet.copy())
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    curSet.append(s[i:j+1])
                    dfs(j+1)
                    curSet.pop()
        
        dfs(0)
        return result
