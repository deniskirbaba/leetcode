class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_zero_idx = None
        for i, n in enumerate(nums):
            if n == 0:
                if left_zero_idx is None:
                    left_zero_idx = i
            elif left_zero_idx is not None:
                nums[left_zero_idx] = n
                nums[i] = 0
                left_zero_idx += 1
        