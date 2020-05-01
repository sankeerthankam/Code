def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) == 0 and len(t) == 0:
        return True

    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        if s_char not in s_dict:
            s_dict[s_char] = t_char
        if t_char not in t_dict:
            t_dict[t_char] = s_char
        if s_dict[s_char] != t_char or t_dict[t_char] != s_char:
            return False
    return True
