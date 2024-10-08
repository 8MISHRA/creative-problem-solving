"""
Given an array as input, print out the array backwards.

E.g, 
Input: [1, 2, 3, 4]
Output: 4, 3, 2, 1

Ignore empty and null arrays.
"""

# Divyansh Mishra
def reverse(arr):
    for i in range(len(arr)):
        print(arr[len(arr)-1-i], end = " ")
    print()

inpt = [1, 2, 3, 4]
reverse(inpt)