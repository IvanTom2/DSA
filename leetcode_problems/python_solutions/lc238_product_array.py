"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    Brute-force
    TIME ERROR ms, 16.7 MB

    Mean time = 282.49118 ms
    Min time  = 280.17159 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        answers = []
        for index in range(len(nums)):
            prod = 1
            for cur in range(len(nums)):
                if cur != index:
                    prod *= nums[cur]
            answers.append(prod)

        return answers


class Solution2(object):
    """
    Wrong solution because 0
    WRONG ANSWER ms, 16.7 MB

    Mean time = 1.05724 ms
    Min time  = 1.05095 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        answers = []
        prod = 1
        for num in nums:
            prod *= num

        for num in nums:
            answers.append(prod // num)

        return answers


class Solution3(object):
    """
    209 ms, 24.3 MB

    Mean time = 2.32207 ms
    Min time  = 8.30223 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        answers = [0 for _ in range((len(nums)))]
        prefix = [0 for _ in range(len(nums))]
        suffix = [0 for _ in range(len(nums))]

        prefix[0] = 1
        suffix[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1)[::-1]:
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            answers[i] = prefix[i] * suffix[i]

        return answers


class Solution4(object):
    """
    195 ms, 23.3 MB

    Mean time = 2.12372 ms
    Min time  = 2.10848 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        answers = [1 for _ in range((len(nums)))]

        current = 1
        for index in range(len(nums)):
            answers[index] *= current
            current *= nums[index]

        current = 1
        for index in range(len(nums))[::-1]:
            answers[index] *= current
            current *= nums[index]

        return answers


if __name__ == "__main__":
    nums = [random.randint(1, 9) for _ in range(1000)]

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    sol4 = Solution4()

    sol1.run(nums)
    sol2.run(nums)
    sol3.run(nums)
    sol4.run(nums)
