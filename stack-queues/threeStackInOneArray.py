"""
Three in One: Describe how you could use a single array to implement three stacks.
"""

class nStackArray(object):
    """
    """
    class Node:
        """
        """
        def __init__(self, value, stackNo) -> None:
            self.value = value
            self.stackNo = stackNo
            self.next = None
            # self.previous = None 

    def __init__(self, n) -> None:
        self.array = []
        self.size = n + 3
        self.stack1Head = self.Node(None, 1)
        self.stack2Head = self.Node(None, 2)
        self.stack3Head = self.Node(None, 3)

    def push(self, stackNo, e):
        """
        Param stack: in which stack to push?
        """
        newNode = self.Node(e, stackNo)

        if stackNo == 1:
            newNode.next = self.stack1Head
            self.stack1Head = newNode
        elif stackNo == 2:
            newNode.next = self.stack2Head
            self.stack2Head = newNode
        elif stackNo == 3:
            newNode.next = self.stack3Head
            self.stack3Head = newNode

        self.stackSizes[stackNo] += 1


    def top(self, stackNo):
        if stackNo == 1 and self.stack1Head:
            return self.stack1Head.value
        elif stackNo == 2 and self.stack2Head:
            return self.stack2Head.value
        elif stackNo == 3 and self.stack3Head:
            return self.stack3Head.value
        else:
            return None

    def pop(self, stackNo):
        if stackNo == 1 and self.stack1Head:
            poppedValue = self.stack1Head.value
            self.stack1Head = self.stack1Head.next
            self.stackSizes[stackNo] -= 1
            return poppedValue
        elif stackNo == 2 and self.stack2Head:
            poppedValue = self.stack2Head.value
            self.stack2Head = self.stack2Head.next
            self.stackSizes[stackNo] -= 1
            return poppedValue
        elif stackNo == 3 and self.stack3Head:
            poppedValue = self.stack3Head.value
            self.stack3Head = self.stack3Head.next
            self.stackSizes[stackNo] -= 1
            return poppedValue
        else:
            return None

    def isEmpty(self, stackNo):
        
        return self.stackSizes[stackNo] == 0 

