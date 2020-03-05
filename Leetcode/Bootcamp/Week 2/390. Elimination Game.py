def lastRemaining(self, n: int) -> int:
    A = [i for i in range(1, n+1)]
    count = 1
    while len(A) != 1:
        if count%2 == 1:
            A = A[1:][::2]
            count = count + 1
        else:
            A = A[::-1][1::2][::-1]
            count = count + 1
    return A[0]
