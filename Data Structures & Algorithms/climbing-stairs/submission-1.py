class Solution:
    # brute force approach
    # def climbStairs(self, n: int) -> int:
    #     return self.climb_stairs(0, n)

    # def climb_stairs(self, i, n):
    #     # i: current step. n: target step
    #     if i > n:
    #         return 0
    #     if i == n:
    #         return 1

    #     return self.climb_stairs(i + 1, n) + self.climb_stairs(i + 2, n)

    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one