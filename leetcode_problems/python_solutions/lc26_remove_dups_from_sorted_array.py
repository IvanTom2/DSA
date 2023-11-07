"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
from time_measure import repeater


class SimplePythonSolution(object):
    """
    Mean time = 0.00165 ms
    Min time  = 0.00120 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> list[int]:
        return len(set(nums))


class Solution1(object):
    """
    Mean time = 0.00479 ms
    Min time  = 0.00360 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return 0

        previous = nums[0]
        index = 1

        while index < len(nums):
            if nums[index] == previous:
                nums.pop(index)
            else:
                previous = nums[index]
                index += 1

        return index


class Solution2(object):
    """
    Mean time = 0.00532 ms
    Min time  = 0.00420 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return 0

        index = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[index] = nums[i + 1]
                index += 1

        return index


class Solution3(object):
    """
    Mean time = 0.00522 ms
    Min time  = 0.00410 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return 0

        maxval = nums[-1]
        index = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[index] = nums[i + 1]
                index += 1
                if nums[i + 1] == maxval:
                    break

        return index


if __name__ == "__main__":
    mnums = [1, 2, 2, 3, 3, 3, 3, 4]
    # nums = [1, 2]

    sol0 = SimplePythonSolution()
    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    sol0.run(nums=mnums[:])
    # sol1.run(nums=mnums[:])

    # sol2.run(nums=mnums[:])
    # sol3.run(nums=mnums[:])
