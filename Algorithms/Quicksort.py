def quicksort(arr, low, high):
    if low < high:
        pivot = _partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)

def _partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = low+1
    while j < high:
        if arr[j] > pivot:
            j += 1
        elif arr[j] == pivot:
            swap(arr, i, j)
            j += 1
        else:
            swap(arr, i, j)
            i += 1
            swap(arr, i, j)
            j += 1
    return i

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr0 = [1,2]
arr1 = []
arr2 = [5]
arr3 = [3, 1]
arr4 = [7,7,7,7,7,7]
arr5 = [3, 1, 2, 3, 3, 1]
arr6 = [0, -1, 5, -3, 2]
arr7 = [-10, 20, 0, -30, 40, 10]
arr8 = [1, 2, 3, 4, 5]
arr9 = [5, 4, 3, 2, 1]
arr10 = [1, 3, -2, 1, 1, -3]

for i in range(11):
    arr = eval(f'arr{i}')

    quicksort(arr, 0, len(arr))
    print(arr)
