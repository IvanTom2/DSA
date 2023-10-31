"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""
from time_measure import repeater


class Solution1(object):
    """
    32 ms, 16.2 MB

    Mean time = 0.00195 ms
    Min time  = 0.00160 ms
    """

    @repeater()
    def run(self, string: str) -> int:
        return len(string.strip().split(" ")[-1])


class Solution2(object):
    """
    33 ms, 16.2 MB

    Mean time = 0.00549 ms
    Min time  = 0.00330 ms
    """

    @repeater()
    def run(self, string: str) -> int:
        end = len(string) - 1

        while end > 0 and string[end] == " ":
            end -= 1

        begin = end
        while begin >= 0 and string[begin] != " ":
            begin -= 1

        return end - begin


class Solution3(object):
    """
    40 ms, 16.2 MB

    Mean time = 0.00566 ms
    Min time  = 0.00460 ms
    """

    @repeater()
    def run(self, string: str) -> int:
        length = len(string)

        count = 0
        for index in range(length)[::-1]:
            if string[index] == " " and count > 0:
                break
            if string[index] != " ":
                count += 1

        return count


class Solution4(object):
    """
    Same solution as Solution3, but without indexing.

    40 ms, 16.2 MB

    Mean time = 0.00566 ms
    Min time  = 0.00460 ms
    """

    @repeater()
    def run(self, string: str) -> int:
        count = 0
        for literal in string[::-1]:
            if literal == " " and count > 0:
                break
            if literal != " ":
                count += 1

        return count


if __name__ == "__main__":
    string = "Hello World"
    string = "   fly me   to   the moon  "

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    sol4 = Solution4()

    sol1.run(string)
    sol2.run(string)
    sol3.run(string)
    sol4.run(string)
