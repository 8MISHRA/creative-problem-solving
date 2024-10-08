def reverse(arr):
    for i in range(len(arr)):
        print(arr[len(arr)-1-i])

arr = [1,2,3,4,5]
print(reverse(arr))


print(input()[::-1], end=" ")
