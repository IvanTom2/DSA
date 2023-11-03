"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]
"""
from time_measure import repeater


class ListNode(object):
    def __init__(self, val: int, next=None) -> None:
        self.val: int = val
        self.next: ListNode = next

    @classmethod
    def from_list(self, array: list[int]):
        head = self(array[0])
        listNode = head
        prev = None

        for index in range(1, len(array)):
            prev = listNode
            listNode = ListNode(array[index])
            prev.next = listNode

        return head

    def to_list(self) -> list:
        array = []
        listNode = self
        while listNode:
            array.append(listNode.val)
            listNode = listNode.next

        return array

    def __repr__(self):
        return rf"{self.to_list()}"


def fillFromList(array: list[int]) -> ListNode:
    head = ListNode(array[0])
    listNode = head
    prev = None

    for index in range(1, len(array)):
        prev = listNode
        listNode = ListNode(array[index])
        prev.next = listNode

    return head


class Solution1(object):
    """
    49 ms, 16.3 MB

    Mean time = 0.00681 ms
    Min time  = 0.00500 ms
    """

    @repeater()
    def run(self, head: ListNode) -> ListNode:
        listNode = head
        while listNode:
            while listNode.next and listNode.val == listNode.next.val:
                listNode.next = listNode.next.next

            listNode = listNode.next

        return head


class Solution2(object):
    """
    Mean time = 0.01191 ms
    Min time  = 0.00850 ms
    """

    @repeater()
    def run(self, listNode: ListNode) -> ListNode:
        newHead = ListNode(listNode.val)
        newListNode = newHead
        prev = None

        while listNode:
            if listNode.val != newListNode.val:
                prev = newListNode
                newListNode = ListNode(listNode.val)
                prev.next = newListNode

            listNode = listNode.next

        return newHead


class Solution3(object):
    """
    35 ms, 16.2 MB

    Mean time = 0.00606 ms
    Min time  = 0.00520 ms
    """

    @repeater()
    def run(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3, 3, 4]

    # listNode = fillFromList(arr)
    listNode = ListNode.from_list(arr)

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    # listNode = sol1.run(listNode)
    # listNode = sol2.run(listNode)
    listNode = sol3.run(listNode)

    print(listNode)
