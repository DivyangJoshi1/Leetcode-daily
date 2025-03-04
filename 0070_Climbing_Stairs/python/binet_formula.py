import math

class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fibN = ((1 + sqrt5) / 2) ** (n + 1) - ((1 - sqrt5) / 2) ** (n + 1)
        return round(fibN / sqrt5)
