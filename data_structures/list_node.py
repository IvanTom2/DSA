from abc import ABC
from typing import Any, Union


class SinglyNode(object):
    def __init__(self, value: Any, next=None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node with value {self.value}"


class AbstractSinglyListNode(ABC):
    def __init__(self, head: SinglyNode = None) -> None:
        self.head: SinglyNode = head


class ClassicSinglyListNode(AbstractSinglyListNode):
    """Classical SLL (Singly Linked List)"""

    def __init__(self, head_node: Union[SinglyNode, Any] = None) -> None:
        self.head: SinglyNode = None

        if head_node:
            self.head = self._nodify(head_node)

    def _nodify(self, entity: Any) -> SinglyNode:
        if isinstance(entity, SinglyNode):
            return entity
        return SinglyNode(entity)

    def _del(self, prevNode: SinglyNode) -> SinglyNode:
        if prevNode is None:
            self.head = self.head.next
            return self.head
        else:
            nextNode = prevNode.next
            prevNode.next = nextNode.next if nextNode else None
            return prevNode.next

    def add_head(self, node: Union[SinglyNode, Any]):
        node = self._nodify(node)

        node.next = self.head
        self.head = node

    def add_back(self, node: Union[SinglyNode, Any]) -> None:
        """This method return the Error if in the ListNode there isn't head"""
        node = self._nodify(node)

        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = node

    def insert(
        self,
        node: Union[SinglyNode, Any],
        position: int,
    ) -> None:
        if position == 0:
            self.add_head(node)
        else:
            node = self._nodify(node)

            prevNode = self.find(position - 1)
            nextNode = prevNode.next

            prevNode.next = node
            node.next = nextNode

    def delpos(
        self,
        position: int = None,
    ) -> SinglyNode:
        prevNode = self.find(position - 1)
        node = self._del(prevNode)
        return node

    def delval(
        self,
        node: Union[SinglyNode, Any],
        maxdel: int = 0,
    ):
        delcount = 0
        node = self._nodify(node)

        prevNode = None
        iterNode = self.head
        while iterNode:
            if iterNode.value == node.value:
                iterNode = self._del(prevNode)
                delcount += 1
            else:
                prevNode = iterNode
                iterNode = iterNode.next

            if maxdel and delcount >= maxdel:
                break

    def find(self, position: int) -> SinglyNode:
        node = self.head
        for _ in range(position):
            if node.next:
                node = node.next
            else:
                raise ValueError("End of the List Node")

        return node

    def reverse(self):
        prev = None
        node = self.head

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

        self.head = prev

    def merge(self, otherSLL: AbstractSinglyListNode) -> None:
        if self.head is None:
            self.head = otherSLL.head
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = otherSLL.head

    def from_list(self, massive: list) -> None:
        """Adding elements of massive to tail of List Node"""

        start_index = 0
        if not self.head:
            self.add_head(massive[0])
            start_index += 1

        for index in range(start_index, len(massive)):
            self.add_back(massive[index])

    def to_list(self) -> list[SinglyNode]:
        massive = []
        node = self.head
        while node:
            massive.append(node.value)
            node = node.next

        return massive

    def get_generator(self):
        def generator():
            node = self.head
            while node:
                yield node
                node = node.next

        return generator()

    def __iter__(self):
        self.cur_node = self.head
        return self

    def __next__(self):
        if self.cur_node is None:
            raise StopIteration

        node = self.cur_node
        self.cur_node = self.cur_node.next

        return node

    def __repr__(self):
        return " -> ".join(map(str, self.to_list()))


class AdvancedSinglyListNode(ClassicSinglyListNode):
    def __init__(self, head_node: Union[SinglyNode, Any] = None) -> None:
        self.head: SinglyNode = None
        self.tail: SinglyNode = None
        self.len = 0

        if head_node != None:
            self.add_head(head_node)
            self.tail = self.head

    def __increment(self, base: int = 1) -> None:
        self.len += base

    def __decrement(self, base: int = 1) -> None:
        self.len -= base

    def _del(self, prevNode: SinglyNode) -> SinglyNode:
        if prevNode is None:
            self.head = self.head.next
            self.__decrement()
            return self.head
        else:
            nextNode = prevNode.next
            prevNode.next = nextNode.next if nextNode else None
            self.__decrement()
            return prevNode.next

    def _count_len(self, otherSLL: AbstractSinglyListNode) -> int:
        counter = 0
        node = otherSLL.head
        while node:
            counter += 1
            node = node.next
        return counter

    def add_head(self, node: Union[SinglyNode, Any]):
        node = self._nodify(node)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.__increment()

    def add_back(self, node: Union[SinglyNode, Any]) -> None:
        """This method return the Error if in the ListNode there isn't head"""
        node = self._nodify(node)
        self.tail.next = node
        self.tail = self.tail.next
        self.__increment()

    def find(self, position: int) -> SinglyNode:
        if position >= self.len:
            raise ValueError("Position > len(ListNode)")
        elif position == self.len - 1:
            return self.tail
        else:
            node = self.head
            for _ in range(position):
                if node.next:
                    node = node.next
                else:
                    raise ValueError("End of the List Node")

            return node

    def insert(
        self,
        node: Union[SinglyNode, Any],
        position: int,
    ) -> None:
        if position == 0:
            self.add_head(node)
        else:
            node = self._nodify(node)

            prevNode = self.find(position - 1)
            nextNode = prevNode.next

            prevNode.next = node
            node.next = nextNode
            self.__increment()

    def merge(self, otherSLL: AbstractSinglyListNode) -> None:
        raise ValueError('TODO: IT IS NOT WORK')
        if self.head is None:
            other_len = 0
            if isinstance(otherSLL, self.__class__):
                other_len = otherSLL.len
            else:
                other_len = self._count_len(otherSLL)
            self.head = otherSLL.head
            self.__increment(other_len)

        else:
            other_len = 0
            if isinstance(otherSLL, self.__class__):
                other_len = otherSLL.len
            else:
                other_len = self._count_len(otherSLL)

            self.tail.next = otherSLL.head
            self.__increment(other_len)


class OddSinglyListNode(object):
    """
    This hipster kind of List Node is bad because contains len of list
    and perform operations only with value (not node).

    It's okay if we insert only one node by operation.
    But it's not okay when we want insert tuple of nodes.
    """

    def __init__(self, head_value: SinglyNode = None) -> None:
        self.head: SinglyNode = None
        self.tail: SinglyNode = None
        self.len = 0

        if head_value != None:
            self.add_head(head_value)

    def __increment(self):
        self.len += 1

    def __decrement(self):
        self.len -= 1

    def add_head(self, value: int) -> None:
        """Adding node at the head if the head not exists"""
        if self.head:
            raise ValueError("Head node exists")

        self.head = SinglyNode(value)
        self.tail = self.head
        self.__increment()

    def add_back(self, value: int) -> None:
        """Adding node at the tail of ListNode"""
        node = SinglyNode(value)
        self.tail.next = node
        self.tail = node
        self.__increment()

    def find(self, position: int) -> SinglyNode:
        node = self.head
        while position:
            node = node.next
            position -= 1
        return node

    def insert_by_position(self, value: int, position: int) -> None:
        """
        Insert node at the position.
        To insert node at the head use 0.
        To insert node at the tail use -1.
        """
        if position == 0:
            oldHead = self.head
            self.head = SinglyNode(value)
            self.head.next = oldHead

        elif position == -1 or position == self.len:
            self.add(value)

        else:
            if position > self.len:
                raise ValueError("Position > maxlen of ListNode")

            prevNode = self.find(position - 1)
            nextNode = prevNode.next

            node = SinglyNode(value)
            prevNode.next = node
            node.next = nextNode

    def delete_by_position(
        self,
        position: int,
        _return: bool = False,
    ) -> None:
        """
        Delete node by position.
        To delete node at the head use 0.
        To delete node at the tail use -1.
        """
        if position > self.len:
            raise ValueError("Position > maxlen of ListNode")

        if position == 0:
            node = self.head
            self.head = node.next

        elif position == -1 or position == self.len:
            node = self.tail
            prev = self.find(self.len - 2)
            self.tail = prev
            self.tail.next = None

        else:
            prev = self.find(position - 1)
            node = prev.next
            prev.next = node.next

        self.__decrement()
        if _return:
            return node

    def to_list(self) -> list[SinglyNode]:
        massive = []
        node = self.head
        while node:
            massive.append(node.value)
            node = node.next

        return massive

    def from_list(self, massive: list) -> None:
        start = 0
        if not self.head:
            self.add_head(massive[0])
            start += 1

        for index in range(start, len(massive)):
            self.add(massive[index])

    def reverse(self) -> None:
        prev = None
        oldHead = self.head
        curr = oldHead

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev
        self.tail = oldHead

    def __iter__(self):
        self.cur_node = self.head
        return self

    def __next__(self):
        if self.cur_node is None:
            raise StopIteration

        node = self.cur_node
        self.cur_node = self.cur_node.next

        return node

    def __repr__(self):
        return " -> ".join(map(str, self.to_list()))


class DoublyNode(object):
    def __init__(
        self,
        value: int,
        next=None,
        prev=None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyListNode(object):
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    massive = [0, 1, 2, 3, 4, 5]

    assl = AdvancedSinglyListNode()
    assl2 = AdvancedSinglyListNode()
    assl3 = ClassicSinglyListNode()

    assl.add_head(0)
    assl.add_back(1)
    assl.add_back(2)

    assl2.add_head(3)
    assl2.add_back(4)
    assl2.add_back(5)

    assl3.add_head(6)
    assl3.add_back(7)
    assl3.add_back(8)

    assl.merge(assl2)
    assl.merge(assl3)

    print(assl)
    print(assl.len)
