"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
"""
import math
from time_measure import repeater


class Solution1(object):
    """
    30 ms, 16.3 MB

    Mean time = 0.00327 ms
    Min time  = 0.00239 ms
    """

    @repeater()
    def run(self, str1: str, str2: str) -> str:
        divisor = ""

        if str1 + str2 == str2 + str1:
            gcd = math.gcd(len(str1), len(str2))
            divisor = (str1 + str2)[:gcd]

        return divisor


if __name__ == "__main__":
    str1, str2 = "ABABAB", "ABAB"

    sol1 = Solution1()

    print(sol1.run(str1, str2))
