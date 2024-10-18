"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""

class MyQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, value):
        """
        Enqueue
        """
        self.inStack.append(value)

    def pop(self):
        """
        Dequeue
        """
        self.shiftStacks() 
        if not self.isEmpty():
            return self.outStack.pop()
        return None  

    def peek(self):
        self.shiftStacks()  
        if not self.isEmpty():
            return self.outStack[-1]
        return None 

    def isEmpty(self):
        return len(self.inStack) == 0 and len(self.outStack) == 0

    def shiftStacks(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
