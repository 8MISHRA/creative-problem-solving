"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure S e t O f S t a c k s that mimics this. S e t O f S t a c k s should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(intindex) which performsa pop operation on a specific sub-stack.
"""

class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])

        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            return None

        value = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return value

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            return None  

        value = self.stacks[index].pop()

        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)

        return value

    def peek(self):
        if not self.stacks:
            return None 

        return self.stacks[-1][-1]

    def isEmpty(self):
        return len(self.stacks) == 0

    def shiftLeft(self, index):
        if index < 0 or index >= len(self.stacks) - 1:
            return

        self.stacks[index].append(self.stacks[index + 1].pop(0))

        if len(self.stacks[index + 1]) == 0:
            self.stacks.pop(index + 1)

setOfStacks = SetOfStacks(3)
setOfStacks.push(1)
setOfStacks.push(2)
setOfStacks.push(3)
setOfStacks.push(4)
setOfStacks.push(5)

print(setOfStacks.stacks)

setOfStacks.popAt(0) 
print(setOfStacks.stacks) 

setOfStacks.pop()
print(setOfStacks.stacks)
