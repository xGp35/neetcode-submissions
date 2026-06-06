class Solution:
    def isValid(self, s: str) -> bool:
        b_dict = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for elem in s:
            if stack and elem in b_dict:
                opening = stack.pop()
                if b_dict[elem] != opening:
                    return False
            elif not stack and elem in b_dict:
                return False
            else:
                stack.append(elem)
        
        return not stack

            