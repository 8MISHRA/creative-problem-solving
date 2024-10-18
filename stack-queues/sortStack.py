"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""

class SortableStack:
    def __init__(self):
        self.stack = [] 

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def isEmpty(self):
        return len(self.stack) == 0

    def sortStack(self):
        tempStack = []
        while not self.isEmpty():
            current = self.pop()
            ######### Interesting Logic ##########
            while tempStack and tempStack[-1] > current:
                self.push(tempStack.pop())
            tempStack.append(current)
        while tempStack:
            self.push(tempStack.pop())


# tests
stack = SortableStack()
stack.push(3)
stack.push(5)
stack.push(1)
stack.push(4)

print("Original Stack:", stack.stack)
stack.sortStack()
print("Sorted Stack:", stack.stack)
