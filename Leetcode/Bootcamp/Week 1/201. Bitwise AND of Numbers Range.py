# Given two numbers m and n
# If n == m, return 0
# If n = m + 1, return n
# Else for all numbers between m and n, perform AND operation between them and return the result

def rangeBitwiseAnd(m, n):
    
    if m - n <= 1:
        return m & n
    
    res = m & m+1
    
    else:
        for i in range(m+2, n+1):
            res = res & i
        return res
