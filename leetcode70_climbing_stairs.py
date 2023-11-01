"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


class Solution1(object):
    """
    Too slow: Runtime Error. Recursive computing with redundant calculations.
    """

    def run(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.run(n - 1) + self.run(n - 2)


class Solution2(object):
    """
    37 ms, 16.2 MB
    """

    def recursion(self, n: int, memo: dict) -> int:
        if n == 0 or n == 1:
            return 1
        elif n not in memo:
            memo[n] = self.recursion(n - 1, memo) + self.recursion(n - 2, memo)
        return memo[n]

    def run(self, n: int) -> int:
        memo = {}
        return self.recursion(n, memo)


class Solution3(object):
    """
    38 ms, 16.2 MB
    """

    def run(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        table = [0] * (n + 1)
        table[0] = table[1] = 1

        for index in range(2, n + 1):
            table[index] = table[index - 1] + table[index - 2]

        return table[n]


class Solution4(object):
    """
    37 ms, 16.2 MB
    """

    def run(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        curr, prev = 1, 1
        for _ in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr


class WrongInPythonSolution5(object):
    def run(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        all_ways, curr, prev = 0, 1, 2
        for _ in range(2, n + 1):
            all_ways = curr + prev
            prev = curr
            curr = all_ways

        return n


if __name__ == "__main__":
    n = 4

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    sol4 = Solution4()
    sol5 = WrongInPythonSolution5()

    sol1.run(n)
    sol2.run(n)
    sol3.run(n)
    sol4.run(n)
    sol5.run(n)
