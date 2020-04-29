def canConstruct(ransomNote, magazine):

    from collections import Counter
    c1 = Counter(ransomNote)
    c2 = Counter(magazine)

    for i in c1:
        if i not in c2 or c1.get(i) > c2.get(i):
            return False
    return True
