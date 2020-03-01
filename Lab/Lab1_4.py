def mySieve(n):
    arr = list(range(n + 1))
    for i in arr:
        if i > 1:
            for j in range(i * i, len(arr), i):
                arr[j] = 0
    arr.sort()
    while arr[0] == 0:
        arr.remove(0)
    return arr
a = 120
print(mySieve(a))