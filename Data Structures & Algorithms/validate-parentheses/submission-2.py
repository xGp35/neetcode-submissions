class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        bracket_dict =  {')':'(', '}':'{', ']':'['} 

        for elem in s:
            if elem in bracket_dict.values():
                stack.append(elem)
            else:
                if len(stack) == 0:
                    return False
                open_b = stack.pop()
                if bracket_dict[elem] != open_b:
                    return False
        if len(stack) == 0:
            return True
        
        return False