from collections import Counter


# O(n^3) solution
#
# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         n_eq = 0
#         for i in range(n):
#             for j in range(n):
#                 eq_flag = True
#                 for k in range(n):
#                     if grid[i][k] != grid[k][j]:
#                         eq_flag = False
#                         break
#                 if eq_flag:
#                     n_eq += 1
#         return n_eq


# O(n^2) solution

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed_grid = zip(*grid)
        c = Counter(map(tuple, grid))
        c_tr = Counter(transposed_grid)
        return sum(c_tr[v] * c[v] for v in c_tr)