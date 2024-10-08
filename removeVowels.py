"""
Given a string, remove all the vowels from the string.

E.g, "hello world" => "hll wrld"
*
"""


# Divyansh Mishra
def removeVowels(s):
    res = ''
    keys = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    keys = 'aeiouAEIOU'
    for i in range(len(s)):
        if s[i] in keys:
            res = res
        else:
            res += s[i]
    return res
print(removeVowels("hello world"))