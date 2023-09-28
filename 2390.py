# Quadratic complexity solution
# 
# class Solution:
#     def removeStars(self, s: str) -> str:
#         while (star_idx := s.find("*")) != -1:
#             s = s.replace(s[star_idx - 1:star_idx + 1], "", 1)
#         return s
    

# from collections import deque


# class Solution:
#     def removeStars(self, s: str) -> str:
#         res = deque()
#         n_stars = 0
#         for ch in s[::-1]:
#             if ch == '*':
#                 n_stars += 1
#             else:
#                 if n_stars > 0:
#                     n_stars -= 1
#                 else:
#                     res.appendleft(ch)
#         return ''.join(res)


class Solution:
    def removeStars(self, s: str) -> str:
        res = list()
        for ch in s:
            if ch == '*':
                res.pop()
            else:
                res.append(ch)
        return ''.join(res)
