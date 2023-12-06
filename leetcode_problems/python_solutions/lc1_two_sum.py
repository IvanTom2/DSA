"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    6069 ms, 17.2 MB

    Mean time = 0.26774 ms
    Min time  = 0.26756 ms
    """

    @repeater(max_repetitions=100)
    def run(self, numbers: list[int], target: int) -> tuple[int]:
        for index1 in range(len(numbers)):
            for index2 in range(len(numbers)):
                if index1 == index2:
                    continue

                if numbers[index1] + numbers[index2] == target:
                    return index1, index2

        return None


class Solution2(object):
    """
    65 ms, 17.7 MB

    Mean time = 0.01423 ms
    Min time  = 0.01295 ms
    """

    @repeater(max_repetitions=100)
    def run(self, numbers: list[int], target: int) -> tuple[int]:
        searched = dict()

        for index in range(len(numbers)):
            search = target - numbers[index]
            if search in searched:
                return index, searched[search]
            else:
                searched[numbers[index]] = index

        return None


if __name__ == "__main__":
    numbers = [random.randint(-1000, 1000) for _ in range(1000)]
    target = numbers[0] + numbers[-1]

    sol1 = Solution1()
    sol2 = Solution2()

    print(sol1.run(numbers, target))
    print(sol2.run(numbers, target))
