def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    len_ = 0
    char_set = set()

    for r in range(len(s)):
        if s[r] not in char_set:
            char_set.add(s[r])
            len_ = max(len_, r-l+1)
        else:
            while s[r] in char_set:
                char_set.remove(s[r])
                l = l+1
    return len_

