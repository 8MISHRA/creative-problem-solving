def maxNum(a, b):
    k = a//b
    k = int(bool(k))
    return a*k + b*(1-k)

print(maxNum(20, 10))