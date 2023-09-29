# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         max_alt, cur_alt = 0, 0
#         for alt_gain in gain:
#             cur_alt += alt_gain
#             max_alt = max(max_alt, cur_alt)
#         return max_alt


# itertools.accumulate solution
from itertools import accumulate
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))