class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return not flowerbed[0]
        flowerbed_iter = iter(range(len(flowerbed)))
        for idx in flowerbed_iter:
            if n == 0:
                return True
            cur = flowerbed[idx]
            if idx == 0:
                post = flowerbed[idx + 1]
                if post == 1:
                    next(flowerbed_iter, None)
                    next(flowerbed_iter, None)
                    continue
                elif cur == 1:
                    next(flowerbed_iter, None)
                    continue
                else:
                    n -= 1
                    next(flowerbed_iter, None)
                    continue
            elif idx == (len(flowerbed) - 1):
                prev = flowerbed[idx - 1]
                if (prev == 0) and (cur == 0):
                    n -= 1
                    break
            else:
                prev = flowerbed[idx - 1]
                post = flowerbed[idx + 1]

                if post == 1:
                    next(flowerbed_iter, None)
                    next(flowerbed_iter, None)
                    continue
                elif cur == 1:
                    next(flowerbed_iter, None)
                    continue
                elif prev == 1:
                    continue
                else:
                    n -= 1
                    next(flowerbed_iter, None)
                    continue

        return n <= 0

