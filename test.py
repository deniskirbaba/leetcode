def findMaxAverage(nums: list[int], k: int) -> float:
    length = len(nums)
    cur_sum = sum(nums[0:k])
    max_sum = cur_sum
    for i in range(k, length):
        cur_sum = cur_sum - nums[i - k] + nums[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum / k

print(findMaxAverage(nums = [0,4,0,3,2], k = 1))
