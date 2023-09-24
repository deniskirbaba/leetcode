class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = dict()
        for num in arr:
            occur[num] = occur.get(num, 0) + 1
        return len(occur) == len(set(occur.values()))