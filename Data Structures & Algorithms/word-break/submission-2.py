class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        # This will be an array of len(s) where each index index represents the portion of s til that index. for example, say target = "abcdef", then dp[0] represents "", dp[1] represents "a", dp[3] represents "abc", etc and the value at that index represents whether the word can be constructed. We will do a look ahead dp where we go over each index of dp, then loop through all word of wordDict dp see what all can be constructed from here.
        dp[0] = True

        for i in range(len(s)+1):
            if dp[i]: #(dp[i] is true)
                for word in wordDict:
                    newWord = s[:i] + word
                    n = len(newWord)
                    if s[:n] == newWord:
                        dp[n] = True
        return dp[len(s)]

                


        
        
        
                        
