def firstUniqChar(s):
    l = len(s)
    for i in range(l):
        ch = s[i]
        if ch not in s[:i]+s[i+1:]:
            return i
    return -1
