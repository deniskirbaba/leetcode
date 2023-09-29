# Brute-force way. Complexity O(n^2)
#
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         res = 0
#         length = len(nums)
#         for i in range(length):
#             n_i = nums[i]
#             if n_i == -1:
#                 continue
#             for j in range(i + 1, length):
#                 n_j = nums[j]
#                 if n_j == -1:
#                     continue
#                 if n_i + n_j == k:
#                     nums[i], nums[j] = -1, -1
#                     res += 1
#                     break
#         return res


# Sorting way. Complexity O(n*log(n)) * O(n) = O(n*log(n))
# 
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         length = len(nums)
#         s_nums = sorted(nums)
#         res = 0
#         left, right = 0, length - 1
#         while left < right:
#             aux = s_nums[left] + s_nums[right]
#             if k == aux:
#                 res += 1
#                 left += 1
#                 right -= 1
#             elif k < aux:
#                 right -= 1
#             else:
#                 left += 1
#         return res


# Dictionary way. Complexity O(n).
#
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        length = len(nums)
        d = dict()
        res = 0
        for n in nums:
            remainder = k - n
            if d.get(remainder, 0) > 0:
                res += 1
                d[remainder] -= 1
            else:
                d[n] = d.get(n, 0) + 1
        return res