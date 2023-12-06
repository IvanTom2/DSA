"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, 
he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
"""
from time_measure import repeater


class Solution1(object):
    """
    40 ms, 16.2 MB

    Mean time = 0.55741 ms
    Min time  = 0.54683 ms
    """

    @repeater()
    def run(self, days: int) -> int:
        amount = 0
        base = 1
        daily = 0

        for _ in range(days):
            amount += base + daily

            daily += 1
            if daily == 7:
                base += 1
                daily = 0

        return amount


class Solution2(object):
    """
    34 ms, 16.2 MB

    Mean time = 0.00255 ms
    Min time  = 0.00222 ms
    """

    @repeater()
    def run(self, days: int) -> int:
        weeks = days // 7
        extra_days = days % 7

        return int(
            28 * weeks
            + 7 * (weeks) * (weeks - 1) / 2
            + weeks * extra_days
            + (extra_days) * (extra_days + 1) / 2
        )


if __name__ == "__main__":
    n = 2000

    sol1 = Solution1()
    sol2 = Solution2()

    print(sol1.run(n))
    print(sol2.run(n))
