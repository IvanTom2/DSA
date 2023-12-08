"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
"""

import random
from time_measure import repeater


class Solution1(object):
    """
    161 ms, 16.7 MB

    Mean time = 8.49118 ms
    Min time  = 8.13203 ms
    """

    @repeater()
    def run(self, flowerbed: list[int], n: int):
        for index in range(len(flowerbed)):
            if n == 0:
                return True

            current = flowerbed[index]
            previous = flowerbed[index - 1] if index - 1 >= 0 else 0
            next = flowerbed[index + 1] if index + 1 < len(flowerbed) else 0

            if current == 0 and previous == 0 and next == 0:
                n -= 1
                flowerbed[index] = 1

        return n == 0


class Solution2(object):
    """
    143 ms, 16.8 MB

    Mean time = 5.15273 ms
    Min time  = 5.07075 ms
    """

    @repeater()
    def run(self, flowerbed: list[int], n: int):
        index = 0
        maxlen = len(flowerbed)

        while index < maxlen and n > 0:
            current = flowerbed[index]
            if current == 0:
                previous = flowerbed[index - 1] if index - 1 >= 0 else 0
                if previous == 0:
                    next = flowerbed[index + 1] if index + 1 < maxlen else 0
                    if next == 0:
                        n -= 1
                        flowerbed[index] = 1

            index += 1

        return n == 0


class Solution3(object):
    """
    147 ms, 16.7 MB

    Mean time = 4.72723 ms
    Min time  = 4.51377 ms
    """

    @repeater()
    def run(self, flowerbed: list[int], n: int):
        flowerbed.insert(0, 0)
        flowerbed.append(0)

        for index in range(1, len(flowerbed) - 1):
            current = flowerbed[index]
            previous = flowerbed[index - 1]
            next = flowerbed[index + 1]

            if (current + previous + next) == 0:
                n -= 1
                flowerbed[index] = 1

        return n <= 0


class Solution4(object):
    """
    144 ms, 16.7 MB

    Mean time = 4.73697 ms
    Min time  = 4.50866 ms
    """

    @repeater()
    def run(self, flowerbed: list[int], n: int):
        start_index = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
            start_index += 1

        flowerbed.append(0)
        for index in range(start_index, len(flowerbed) - 1):
            current = flowerbed[index]
            previous = flowerbed[index - 1]
            next = flowerbed[index + 1]

            if (current + previous + next) == 0:
                n -= 1
                flowerbed[index] = 1

        return n <= 0


if __name__ == "__main__":
    n = 10000
    flowerbed = [random.randint(0, 1) for _ in range(n)]

    # flowerbed = [1, 0, 0, 0, 1]
    # flowerbed = [1, 0, 1, 0, 1]
    # flowerbed = [0, 0, 1, 0, 0]
    # n = 1

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    sol4 = Solution4()

    # print(sol1.run(flowerbed, n))
    # print(sol2.run(flowerbed, n))
    print(sol3.run(flowerbed, n))
    # print(sol4.run(flowerbed, n))
