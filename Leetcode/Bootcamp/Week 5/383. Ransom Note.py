def canConstruct(ransomNote, magazine):

    from collections import Counter
    c1 = Counter(ransomNote)
    c2 = Counter(magazine)

    for i in c1:
        if i not in c2 or c1.get(i) > c2.get(i):
            return False
    return True


def canConstruct(ransomNote, magazine):

    from collections import Counter

    c1 = Counter(ransomNote)
    c2 = Counter(magazine)

    if c1 - c2 == 0:
        return True
    else:
        return False

def canConstruct(ransomNote, magazine):

    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i) or i not in magazine:
            return False
    return True
