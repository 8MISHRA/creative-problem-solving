"""
Stack Min: How would you design a stack which, in addition to p u s h and pop, has a function m i n
which returns the minimum eiement? Push, p o p and m i n should ail operate in 0 ( 1 ) time.

Assumption: All elements are distinct.

"""

class MinStack:
    def __init__(self):
        self.stack = []       
        self.minStack = []

    def push(self, value):
        self.stack.append(value)
        
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)

    def pop(self):
        if not self.stack:
            return None
        
        poppedValue = self.stack.pop()
        
        if poppedValue == self.minStack[-1]:
            self.minStack.pop()

        return poppedValue

    def min(self):
        if not self.minStack:
            return None 
        return self.minStack[-1]

    def top(self):
        if not self.stack:
            return None 
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0
