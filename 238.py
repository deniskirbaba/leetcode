class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     length = len(nums)
    #     answer = [1] * length
    #     for i in range(length):
    #         for j in (k for k in range(length) if k != i):
    #             answer[j] *= nums[i]
    #     return answer

    def prefix(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        for i in range(1, length):
            res[i] = res[i - 1] * nums[i - 1]
        return res
    
    def postfix(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        for i in range(length - 2, -1, -1):
            res[i] = res[i + 1] * nums[i + 1]
        return res
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        prefix = 1
        postfix = 1
        for i in range(length):
            res[i] *= prefix
            prefix *= nums[i]
            res[length - i - 1] *= postfix
            postfix *= nums[length - i - 1]
        return res
