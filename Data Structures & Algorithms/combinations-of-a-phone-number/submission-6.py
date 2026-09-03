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

        resPerms = [""]
        for digit in digits:
            temp = []
            for p in resPerms:
                for char in digit_map[digit]:
                    temp.append(p + char)
            resPerms = temp
        
        return resPerms