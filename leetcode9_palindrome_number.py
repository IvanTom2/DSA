"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


class Solution(object):
    """52 ms, 16.1 MB"""

    def run(self, x: int) -> bool:
        origin = list(str(x))
        reverse = origin[::-1]
        return origin == reverse


class Solution2(object):
    """52 ms, 16.1 MB"""

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
    """54 ms, 16.3 MB"""

    def run(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10


if __name__ == "__main__":
    integer = 10

    sol = Solution()
    sol = Solution2()
    sol = Solution3()

    print(sol.run(integer))
