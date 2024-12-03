'''
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.
'''

def smallestDiff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    minDiff = float('inf')
    while i < len(arr1) and j < len(arr2):
        minDiff = min(minDiff, abs(arr1[i] - arr2[j]))
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return minDiff
print(smallestDiff([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))   