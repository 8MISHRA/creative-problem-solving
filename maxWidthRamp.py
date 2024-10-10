"""
Leetcode Problem of the day: 11/10/2024
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

"""


def maxWidthRamp(nums):
    result = 0
    stack = []
    index = {}
    for i in range(len(nums)):
        if len(stack) == 0:
            stack.append(nums[i])
            if nums[i] not in index:
                index[nums[i]] = i
        elif nums[i] < stack[-1]:
            stack.append(nums[i])
            if nums[i] not in index:
                index[nums[i]] = i
        else:
            idx = -1
            while idx > -len(stack) and nums[i] >= stack[idx-1]:
                idx -= 1
            j = index[stack[idx]]
            result = (i-j) if (i-j) > result else result
    return result

arr = [9,8,1,0,1,9,4,0,4,1]
# arr = [6,0,8,2,1,5]
res = maxWidthRamp(arr)
print(res)