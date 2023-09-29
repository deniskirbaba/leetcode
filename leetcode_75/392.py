class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        l_s = len(s)
        l_t = len(t)
        s_i = 0
        for t_i in range(l_t):
            if t[t_i] == s[s_i]:
                s_i += 1
            if s_i == l_s:
                return True
