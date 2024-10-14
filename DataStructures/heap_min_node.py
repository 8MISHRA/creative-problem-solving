from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class MinHeap:
    def __init__(self):
        self.root = None
        self.size = 0
        self.insert_queue = deque()

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty heap")
        return self.root.key

    def insert(self, key):
        new_node = Node(key)
        self.size += 1

        if self.root is None:
            self.root = new_node
            self.insert_queue.append(self.root)
            return

        parent = self.insert_queue[0]

        if parent.left is None:
            parent.left = new_node
        elif parent.right is None:
            parent.right = new_node
            self.insert_queue.popleft()
        new_node.parent = parent
        self.insert_queue.append(new_node)

        self._percolate_up(new_node)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Extract from empty heap")
        min_key = self.root.key

        if self.size == 1:
            self.root = None
            self.insert_queue.pop()
            self.size -= 1
            return min_key

        last_node = self._last_node()
        self.root.key = last_node.key

        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
            self.insert_queue.append(last_node.parent)

        self.size -= 1

        if last_node in self.insert_queue:
            self.insert_queue.remove(last_node)

        self._percolate_down(self.root)

        return min_key

    def _last_node(self):
        queue = deque([self.root])
        last = None
        while queue:
            last = queue.popleft()
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)
        return last

    def _percolate_up(self, node):
        while node.parent and node.key < node.parent.key:
            node.key, node.parent.key = node.parent.key, node.key
            node = node.parent

    def _percolate_down(self, node):
        while node:
            smallest = node
            if node.left and node.left.key < smallest.key:
                smallest = node.left
            if node.right and node.right.key < smallest.key:
                smallest = node.right
            if smallest != node:
                node.key, smallest.key = smallest.key, node.key
                node = smallest
            else:
                break

    def __str__(self):
        if not self.root:
            return "Empty Heap"

        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(str(node.key))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return "Heap: " + ", ".join(result)

if __name__ == "__main__":
    heap = MinHeap()
    elements = [20, 15, 30, 10, 8, 25, 40]

    print("Inserting elements:")
    for elem in elements:
        heap.insert(elem)
        print(heap)

    print("\nExtracting minimum elements:")
    while not heap.is_empty():
        min_elem = heap.extract_min()
        print(f"Extracted: {min_elem}")
        print(heap)
