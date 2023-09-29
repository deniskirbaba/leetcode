class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n_zeros = 1
        left = 0
        for right, n in enumerate(nums):
            n_zeros -= 1 - n
            if n_zeros < 0:
                n_zeros += 1 - nums[left]
                left += 1
        return right - left 