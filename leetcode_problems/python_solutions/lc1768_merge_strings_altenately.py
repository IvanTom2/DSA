"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""
from time_measure import repeater
from itertools import zip_longest


class Solution1(object):
    """
    35 ms, 16.4 MB

    Mean time = 0.01382 ms
    Min time  = 0.01265 ms
    """

    @repeater()
    def run(self, str1: str, str2: str) -> str:
        minword = str1 if len(str1) <= len(str2) else str2
        maxword = str1 if minword == str2 else str2

        merged = ""
        for i in range(len(minword)):
            merged += str1[i]
            merged += str2[i]

        for i in range(len(minword), len(maxword)):
            merged += maxword[i]

        return merged


class Solution2(object):
    """
    38 ms, 16.3 MB

    Mean time = 0.03970 ms
    Min time  = 0.03810 ms
    """

    @repeater()
    def run(self, str1: str, str2: str) -> str:
        merged = ""

        i = 0
        while i < len(str1) or i < len(str2):
            if i < len(str1):
                merged += str1[i]
            if i < len(str2):
                merged += str2[i]

            i += 1

        return merged


class Solution3(object):
    """
    38 ms, 16.4 MB

    Mean time = 0.17119 ms
    Min time  = 0.16548 ms
    """

    @repeater()
    def run(self, str1: str, str2: str) -> str:
        return "".join(a + b for a, b in zip_longest(str1, str2, fillvalue=""))


if __name__ == "__main__":
    str1 = "abcaadsgasdfgasdgasdgasdgasdgasdgfasdfasdf"
    str2 = "pqrzzasdfasdfasdgasdgasdfasdasdfasfasdfasdfasdf"

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    print(sol3.run(str1, str2))
