class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            if token in ("+", "-", "*", "/"):
                a = stack.pop()
                b = stack.pop()
                
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(b-a)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    stack.append(int(b/a))
        
        return stack[-1]
                    