"""
You are given a string num, representing a large integer. 
Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
"""
from time_measure import repeater


class Solution1(object):
    """
    55 ms, 18 MB

    Mean time = 0.01576 ms
    Min time  = 0.01450 ms
    """

    odd = set(["1", "3", "5", "7", "9"])

    @repeater()
    def run(self, number: str) -> str:
        for index in range(len(number))[::-1]:
            char = number[index]

            if char in self.odd:
                return number[: index + 1]

        return ""


class Solution2(object):
    """
    45 ms, 17.8 MB

    Mean time = 0.02608 ms
    Min time  = 0.02468 ms
    """

    @repeater()
    def run(self, number: str) -> str:
        for index in range(len(number))[::-1]:
            char = number[index]

            if int(char) & 1:
                return number[: index + 1]

        return ""


if __name__ == "__main__":
    number = "525123024680024680024680024680024680024680024680024680024680024680"

    sol1 = Solution1()
    sol2 = Solution2()

    print(sol1.run(number))
    print(sol2.run(number))
