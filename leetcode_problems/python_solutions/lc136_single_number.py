"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
"""
from time_measure import repeater


class Solution1(object):
    """
    115 ms, 18.9 MB

    Mean time = 0.00970 ms
    Min time  = 0.00380 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        memo = {}

        index = len(nums) - 1
        while index >= 0:
            memo[nums[index]] = memo.get(nums[index], 0) + 1
            index -= 1

        for key, value in memo.items():
            if value == 1:
                return key


class Solution2(object):
    """
    126 ms, 18.8 MB

    Mean time = 0.00303 ms
    Min time  = 0.00170 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor


if __name__ == "__main__":
    nums = [2, 2, 1]

    sol1 = Solution1()
    sol2 = Solution2()

    # print(sol1.run(nums))
    print(sol2.run(nums))
