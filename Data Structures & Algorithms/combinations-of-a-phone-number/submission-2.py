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

        res = [""]

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in digit_map[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res


            

        
