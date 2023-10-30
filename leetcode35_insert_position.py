"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
"""


class Solution(object):
    def binary_search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start

    def run(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target)


if __name__ == "__main__":
    nums = [1, 3]
    target = 0

    sol = Solution()
    print(sol.run(nums, target))
