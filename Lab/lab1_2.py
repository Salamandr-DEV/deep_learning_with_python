def myFib(num):
    first = 1
    second = 1
    result = 0
    for i in range(3,num+1):
        result = first + second
        second = first
        first = result
    if num == 1:
        return first
    if num == 2:
        return second
    else:
        return result
n = 8
print(myFib(n))
