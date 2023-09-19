# Queue method


# from queue import SimpleQueue


# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         memory_zeros = SimpleQueue()
#         max_ones = 0
#         cur_ones, cur_zeros = 0, 0
#         for idx, num in enumerate(nums):
#             if num == 1:
#                 cur_ones += 1
#             elif k == 0:
#                 max_ones = max(max_ones, cur_ones)
#                 cur_ones = 0
#             else:
#                 if cur_zeros < k:
#                     memory_zeros.put_nowait(idx)
#                     cur_zeros += 1
#                     cur_ones += 1
#                 else:
#                     max_ones = max(max_ones, cur_ones)
#                     cur_ones = idx - memory_zeros.get_nowait()
#                     memory_zeros.put_nowait(idx)
#         return max(max_ones, cur_ones)
            


# Slide-window with variable length

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left, right = 0, 0
        cur_zeros = 0
        max_ones = 0
        while right < length:
            if nums[right] == 0:
                max_ones = max(right - left, max_ones)
                if cur_zeros < k:
                    cur_zeros += 1
                else:
                    while nums[left] == 1:
                        left += 1
                    left += 1
            right += 1
        return max(right - left, max_ones)



    # def longestOnes(self, A, K):
    #     i = 0
    #     for j in xrange(len(A)):
    #         K -= 1 - A[j]
    #         if K < 0:
    #             K += 1 - A[i]
    #             i += 1
    #     return j - i + 1