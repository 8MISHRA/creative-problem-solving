def sort_anagram(arr):

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if is_permutation(arr[i], arr[j]):
                # print("swapping {arr[i]} and {arr[j]}")
                swap(arr, i, j)
    return arr 


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp



def is_permutation(s1, s2):
    store = {}
    sum = 0
    for c in s1:
        if c in store:
            store[c] = store[c] + 1  
        else:
            store[c] = 1

    for c in s2:
        if c in store:
            store[c] = store[c] - 1  
        else:
            return False
    
    for i in store.values():
        sum += i 
    # print(store)
    return sum == 0


anagrams = [
  "listen", "tar", "dog", "viel",
  "evil", "vile", "live", "tinsel",
  "rat", "silent", "gdo",
  "god", "enlist", "dog", "rta"
]

sort_anagram(anagrams)
print(anagrams)



