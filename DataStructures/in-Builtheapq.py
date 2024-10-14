import heapq

# List of integers
arr = [10, 20, 15, 30, 40]

# Negate the elements to simulate a max heap
max_heap = [-x for x in arr]
heapq.heapify(max_heap)

# To get the maximum element
max_element = -heapq.heappop(max_heap)
print(max_element)
# Printing the heap
print([-x for x in max_heap])  # Convert back to the original values
print(f"Max element: {max_element}")
