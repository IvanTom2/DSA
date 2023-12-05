"""
You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. 
A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. 
A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

Example 1:

Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.

"""
from time_measure import repeater


class Solution1(object):
    """
    40 ms, 16.3 MB

    Mean time = 0.01382 ms
    Min time  = 0.01265 ms
    """

    @repeater()
    def run(self, number: int) -> int:
        total = 0
        while number > 1:
            if number % 2 == 0:
                number = number / 2
                total += number
            else:
                total += (number - 1) / 2
                number = ((number - 1) / 2) + 1

        return int(total)


class Solution2(object):
    """
    33 ms, 16.3 MB

    Mean time = 0.00154 ms
    Min time  = 0.00112 ms
    """

    @repeater()
    def run(self, number: int) -> int:
        return number - 1


if __name__ == "__main__":
    sol1 = Solution1()
    sol2 = Solution2()

    print(sol1.run(220000))
    print(sol2.run(220000))
