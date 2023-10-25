"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution(object):
#     def run(
#         self,
#         list1: list[int],
#         list2: list[int],
#     ) -> list[int]:
#         newlist = []
#         while list1 or list2:
#             if list1 and list1[0] <= list2[0]:
#                 newlist.append(list1.next())
#             else:
#                 newlist.append(list2.next())

#         return newlist


if __name__ == "__main__":
    list1 = ListNode()
    list1 = list1.next()

    print(list1.val)

    # list1 = [1, 2, 3]
    # list2 = [1, 1, 1, 2, 3]

    # sol = Solution()
    # print(sol.run(list1, list2))
