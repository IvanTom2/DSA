"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    42 ms, 16.2 MB

    Mean time = 0.88442 ms
    Min time  = 0.86408 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        max1, max2 = 0, 0

        for num in nums:
            if num > max2:
                if num > max1:
                    temp = max1
                    max1 = num
                    max2 = temp
                else:
                    max2 = num

        return (max1 - 1) * (max2 - 1)


class Solution2(object):
    """
    54 ms, 16.4 MB

    Mean time = 0.41487 ms
    Min time  = 0.40841 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        max1 = max(nums)
        nums.pop(nums.index(max1))
        max2 = max(nums)

        return (max1 - 1) * (max2 - 1)


if __name__ == "__main__":
    nums = [random.randint(-2000, 1000) for _ in range(10000)]

    sol1 = Solution1()
    sol2 = Solution2()

    print(sol1.run(nums))
    # print(sol2.run(nums))
