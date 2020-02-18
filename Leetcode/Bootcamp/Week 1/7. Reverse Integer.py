def reverse(x):

    negative = False

    if x < 0:
        negative = True
        x = -x

    rev = 0
    while x:
        # dig = temp % 10
        rev = rev * 10 + (x % 10)
        x = x // 10

    if rev > pow(2, 31):
        return 0
    else:
        return rev*-1 if negative else rev
