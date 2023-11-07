"""
LeetCode problem 13.
Roman to Integer

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Input: s = "III"
Output: 3
Explanation: III = 3.
"""
from time_measure import repeater


class Solution1(object):
    """
    61 ms, 16.3 MB

    Mean time = 0.01264 ms
    Min time  = 0.01140 ms
    """

    vdict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def summer(self, massive: list[int]) -> int:
        _len = len(massive)
        _sum = 0
        for index in range(_len):
            if (index < _len - 1) and (massive[index] < massive[index + 1]):
                massive[index + 1] -= massive[index]
            else:
                _sum += massive[index]

        return _sum

    @repeater()
    def run(self, string: str) -> int:
        massive = list(map(lambda s: self.vdict[s], string))
        return self.summer(massive)


class Solution2(object):
    """
    40 ms, 16.2 MB

    Mean time = 0.00806 ms
    Min time  = 0.00630 ms
    """

    vdict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    @repeater()
    def run(self, string: str) -> int:
        number = 0

        string = string.replace("IV", "IIII").replace("IX", "VIIII")
        string = string.replace("XL", "XXXX").replace("XC", "LXXXX")
        string = string.replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in string:
            number += self.vdict[char]

        return number


class Solution3(object):
    """
    52 ms, 16.3 MB

    Mean time = 0.00692 ms
    Min time  = 0.00550 ms
    """

    vdict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    @repeater()
    def run(self, string: str) -> int:
        number = 0
        previous_number = 0

        for symbol in string[::-1]:
            if self.vdict[symbol] >= previous_number:
                number += self.vdict[symbol]
            else:
                number -= self.vdict[symbol]
            previous_number = self.vdict[symbol]

        return number


if __name__ == "__main__":
    string = "XIV"
    string = "IXIV"
    string = "MCMXCIV"

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    sol1.run(string)
    sol2.run(string)
    sol3.run(string)
