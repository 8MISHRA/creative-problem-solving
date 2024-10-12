'''
This solution needs to be better, since this is not in place, Or you can also avoid using string as a result since it is being 
recreated eerytime you modify it
'''


def URLify(s, trueLength):
    res = [] 
    result = ""
    s_lst = list(s)
    i = trueLength-1
    j = len(s_lst)-1
    while i >= 0:
        if s_lst[i] != " ":
            result = s_lst[i] + result
            i -= 1
        else:
            i -= 1
            result = "%20" + result
    return result

s = "My name is john         "
print(URLify(s, 15))

