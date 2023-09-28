class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = list()
        for ast in asteroids:
            if (not res) or ast > 0:
                res.append(ast)
            else:
                while res:
                    if res[-1] < 0:
                        res.append(ast)
                        break
                    elif (ast + res[-1]) < 0:
                        if len(res) == 1:
                            res[-1] = ast
                            break
                        else:
                            res.pop()
                    elif (ast + res[-1]) == 0:
                        res.pop()
                        break
                    else:
                        break
        return res
                