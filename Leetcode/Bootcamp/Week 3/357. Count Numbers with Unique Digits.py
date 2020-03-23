# https://www.youtube.com/watch?v=OkJKxoDbQ_c

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91

    s = 1
    for i in range(1,n+1):
        s+=9*math.factorial(9)//math.factorial(10-i)  #count for i-digit numbers
    return s
