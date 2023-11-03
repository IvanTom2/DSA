"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""


class Solution1(object):
    """
    34 ms, 16.3 MB
    """

    def run(
        self,
        nums1: list[int],
        m: int,
        nums2: list[int],
        n: int,
    ) -> None:
        index1 = m - 1
        index2 = n - 1
        pointer = m + n - 1

        while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[pointer] = nums1[index1]
                index1 -= 1
            else:
                nums1[pointer] = nums2[index2]
                index2 -= 1

            pointer -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3

    nums2 = [2, 5, 6]
    n = 3

    sol1 = Solution1()

    print(sol1.run(nums1, m, nums2, n))
