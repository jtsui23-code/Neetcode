

class MinStack:

    def __init__(self):
        self.stack = []

        self.min_stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)

        if type(val) == int:
            if self.min is None:
                self.min = val
                self.min_stack.append(None)

            elif self.min > val:
                self.min_stack.append(self.min)
                self.min = val
                
            else:
                self.min_stack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
       return self.min
        
