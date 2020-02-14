def rangeBitwiseAnd(m, n):
    
    if m - n <= 1:
        return m & n
    
    res = m & m+1
    
    else:
        for i in range(m+2, n+1):
            res = res & i
        return res
