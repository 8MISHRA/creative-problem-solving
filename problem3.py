"""
Key take ays:
1. Don't use any built-in functions
2. Case sensitivity is important
3. If the string is empty, return an empty string
"""

def removeVowels(s):
    lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in s:
        if i in lst:
            s = s.replace(i, "")
    return s 
print(removeVowels("hello world"))