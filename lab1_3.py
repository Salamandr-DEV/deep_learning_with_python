def isPalindrom(string):
    strn = str(string)
    a = len(strn)
    b = True
    for i in range(a):
        if strn[i] == strn[a-i-1]:
            b = True
        else:
            b = False
            break
    return b
str2 = "abba"
print(isPalindrom(str2))

