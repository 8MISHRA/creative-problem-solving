"""
how to make it?
Pointer based approach, how to solve this?

by now, I am just talking about 3 stacks in an array
How, How can I solve this
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
            self.previous = None 

    def __init__(self, n) -> None:
        self.array = []
        self.size = n + 3
        self.stack1Head = self.Node(None, 1)
        self.stack2Head = self.Node(None, 2)
        self.stack3Head = self.Node(None, 3)

    def push(self, stackNo, e):
        """
        param stack: in which stack to push?
        """
