"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""
from time_measure import repeater
import time


class Solution1(object):
    """
    52 ms, 16.1 MB

    Mean time = 0.00236 ms
    Min time  = 0.00210 ms
    """

    @repeater()
    def run(self, x: int) -> bool:
        origin = list(str(x))
        reverse = origin[::-1]
        return origin == reverse


class Solution2(object):
    """
    52 ms, 16.1 MB

    Mean time = 0.01471 ms
    Min time  = 0.01230 ms
    """

    @repeater()
    def run(self, x: int) -> bool:
        if x >= 0:
            reversed_num = 0
            temp_num = x

            while temp_num != 0:
                digit = temp_num % 10
                reversed_num = reversed_num * 10 + digit
                temp_num //= 10

            if x == reversed_num:
                return True

        return False


class Solution3(object):
    """
    54 ms, 16.3 MB

    Mean time = 0.00925 ms
    Min time  = 0.00700 ms
    """

    @repeater()
    def run(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10


if __name__ == "__main__":
    start = time.time()

    integer = 111111122222222111111

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    sol1.run(integer)
    sol2.run(integer)
    sol3.run(integer)

    print(time.time() - start)
