class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev = nums[0]
        mon_inc = True
        mon_dec = True
        for i in range(1, len(nums)):
            if nums[i] > prev:
                mon_dec = False
            elif nums[i] < prev:
                mon_inc = False
            if not (mon_dec or mon_inc):
                return False
            prev = nums[i]
        return True