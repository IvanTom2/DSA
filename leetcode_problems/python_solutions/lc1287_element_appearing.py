"""
Given an integer array sorted in non-decreasing order, there is exactly one 
integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    88 ms, 18 MB

    Mean time = 3.71075 ms
    Min time  = 3.62489 ms
    """

    @repeater()
    def run(self, array: list[int]) -> int:
        maxcount = len(array)
        mapper = dict()

        for num in array:
            if num in mapper:
                mapper[num] += 1
            else:
                mapper[num] = 1

        for key, value in mapper.items():
            if value / maxcount > 0.25:
                return key

        return None


class Solution2(object):
    """
    80 ms, 17.6 MB

    Mean time = 3.39732 ms
    Min time  = 3.33288 ms
    """

    @repeater()
    def run(self, array: list[int]) -> int:
        if len(array) == 1:
            return array[0]

        maxcount = len(array)
        mapper = dict()

        for num in array:
            if num in mapper:
                mapper[num] += 1
                if mapper[num] / maxcount > 0.25:
                    return num
            else:
                mapper[num] = 1

        return None


class Solution3(object):
    """
    73 ms, 17.6 MB

    Mean time = 0.02540 ms
    Min time  = 0.02374 ms
    """

    def firstOccurence(
        self,
        numbers: list[int],
        target: int,
    ) -> int:
        start = 0
        end = len(numbers) - 1

        while start < end:
            mid = start + (end - start) // 2
            if numbers[mid] < target:
                start = mid + 1
            else:
                end = mid

        return end

    @repeater()
    def run(self, array: list[int]) -> int:
        if len(array) == 1:
            return array[0]

        maxlen = len(array)
        quarters = [
            array[maxlen // 4],
            array[maxlen // 2],
            array[maxlen * 3 // 4],
        ]

        for quartedNum in quarters:
            position = self.firstOccurence(array, quartedNum)
            if array[position + maxlen // 4] == quartedNum:
                return quartedNum

        return -1


if __name__ == "__main__":
    maxlen = 10000
    targets = [maxlen + 1 for _ in range(int(0.26 * 10000))]
    others = [random.randint(0, maxlen) for _ in range(int(0.74 * 10000))]
    array = targets + others
    array.sort()

    # sol1 = Solution1()
    # sol2 = Solution2()
    sol3 = Solution3()

    # print(sol1.run(array))
    # print(sol2.run(array))
    print(sol3.run(array))
