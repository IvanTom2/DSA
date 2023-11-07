"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
from time_measure import repeater


class Solution1(object):
    """
    37 ms, 16.1 MB

    Mean time = 0.00508 ms
    Min time  = 0.00270 ms
    """

    @repeater()
    def run(self, digits: list[int]) -> list[int]:
        length = len(digits) - 1

        while digits[length] == 9:
            digits[length] = 0
            length -= 1

        if length < 0:
            digits = [1] + digits
        else:
            digits[length] += 1

        return digits


class Solution2(object):
    """
    39 ms, 16.1MB

    Mean time = 0.00365 ms
    Min time  = 0.00220 ms
    """

    @repeater()
    def run(self, digits: list[int]) -> list[int]:
        for index in range(len(digits))[::-1]:
            if digits[index] < 9:
                digits[index] += 1
                return digits
            digits[index] = 0

        return [1] + digits


if __name__ == "__main__":
    digits = [8, 9, 9, 9]

    sol1 = Solution1()
    sol2 = Solution2()

    sol1.run(digits)
    sol2.run(digits)
