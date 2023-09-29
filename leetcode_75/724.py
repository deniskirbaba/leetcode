# Bad solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_idx = -1
        s = sum(nums)
        r_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            s -= nums[i]
            if s == r_sum:
                pivot_idx = i
            r_sum += nums[i]
        return pivot_idx