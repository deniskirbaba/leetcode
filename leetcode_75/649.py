from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        i = len(senate)
        while dire and radiant:
            d = dire.popleft()
            r = radiant.popleft()
            if d < r:
                dire.append(i)
            else:
                radiant.append(i)
            i += 1
        if dire:
            return 'Dire'
        else:
            return 'Radiant'


s = Solution()
print(s.predictPartyVictory('RDRDRDRDRD'))
