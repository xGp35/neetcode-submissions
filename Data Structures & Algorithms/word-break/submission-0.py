class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #canConstruct
        memo = {}
        def helper(target):
            if target in memo: return memo[target]
            if target == "": return True

            for word in wordDict:
                if target.startswith(word):
                    suffix = target[len(word):]
                    if helper(suffix):
                        memo[target] = True
                        return True

            memo[target] = False
            return False
        return helper(s)
                    
                        
                     