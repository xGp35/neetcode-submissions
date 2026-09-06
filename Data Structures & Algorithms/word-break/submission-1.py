class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(target):
            if target in memo: return memo[target]
            if target == "": return True
            
            for word in wordDict:
                if target.startswith(word):
                    remainder = target[len(word):]
                    remainderResult = dfs(remainder)
                    if remainderResult:
                        memo[target] = True
                        return True
            memo[target] = False
            return False
        
        return dfs(s)
                        
