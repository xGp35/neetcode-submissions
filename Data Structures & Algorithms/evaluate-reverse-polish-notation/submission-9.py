class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()
        operations = {'+', '-', '*', '/'}
        for elem in tokens:
            if elem not in operations:
                stack.append(int(elem))
            else:
                b = stack.pop()
                a = stack.pop()
                if elem == '+':
                    stack.append(a + b)
                elif elem == '-':
                    stack.append(a - b)
                elif elem == '*':
                    stack.append(a * b)
                else:  # '/'
                    stack.append(int(a / b))
                
        return stack.pop()
                
            
