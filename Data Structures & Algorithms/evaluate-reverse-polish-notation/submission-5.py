class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operator = {'+', '-', '*', '/'}

        for elem in tokens:
            print(stack)
            if elem not in operator:
                stack.append(int(elem))
            else:
                b = stack.pop()
                a = stack.pop()
                if elem == '+':
                    stack.append(a+b)
                elif elem == '-':
                    stack.append(a-b)
                elif elem == '*':
                    stack.append(a*b)
                elif elem == '/':
                    stack.append(int(a / b))
        return stack.pop()
            
            