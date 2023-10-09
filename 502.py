import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # dict + list method
        # time limit exceeded
        #
        # projects = dict()
        # for profit, cap in zip(profits, capital):
        #     if profit != 0:
        #         projects.setdefault(profit, list()).append(cap)

        # profit_variants = sorted(projects.keys(), reverse=True)
        # for profit in projects:
        #     projects[profit].sort(reverse=True)

        # for i in range(k):
        #     for profit in profit_variants:
        #         if projects[profit][-1] <= w:
        #             w += profit
        #             projects[profit].pop()
        #             if not projects[profit]:
        #                 del projects[profit]
        #                 profit_variants.remove(profit)
        #             break

        # return w


        # sort method
        # time limit exceeded
        #
        # projects = list()
        # for profit, cap in zip(profits, capital):
        #     projects.append((profit, cap))
        # projects.sort(key=lambda proj: (proj[0], -proj[1]))
        
        # for i in range(k):
        #     for j in range(len(projects) - 1, -1, -1):
        #         if projects[j][1] <= w:
        #             w += projects.pop(j)[0]
        #             break
        
        # return w


        # priorityqueue method
        heap = []
        projects = sorted(zip(profits, capital), key=lambda proj: proj[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap: 
                w -= heapq.heappop(heap)
        return w



    

s = Solution()
res = s.findMaximizedCapital(k=5,
                       w=5,
                       profits=[1, 2, 3, 4, 5, 6, 7],
                       capital=[5, 5, 5, 5, 3, 2, 1])
print(res)