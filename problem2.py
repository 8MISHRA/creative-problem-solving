'''
Given a matrix as input (2D array). Print out all the items in that array:

E.g, Input: [ [1 2 3], [4,5,6], [7,8,9]]
'''

def print_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print("\n")

arr = [[1, 2, 3], [4,5,6], [7,8,9]]
print(print_matrix(arr))