class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        digit_map={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def dfs(i, curSet):
            if len(curSet) == len(digits):
                result.append(''.join(curSet))
                return
            

            for char in digit_map[digits[i]]:
                dfs(i+1, curSet + char)
        
        dfs(0, "")
        return result


            

        
