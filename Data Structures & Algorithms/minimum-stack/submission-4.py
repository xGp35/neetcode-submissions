class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # ith element stores the min value till that point

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1]) 
        return

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]