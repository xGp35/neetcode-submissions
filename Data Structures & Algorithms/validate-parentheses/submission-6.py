class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        b_dict = {')':'(', ']':'[', '}':'{'}

        for b in s:
            if b in ('(', '{','['):
                stack.append(b)
            else:
                if not stack or b_dict[b] != stack[-1]:
                    return False
                stack.pop()
        
        return stack == []