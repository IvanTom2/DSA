from abc import ABC
from typing import Any, Union


class AbstractNode(ABC):
    def __init__(self, value: Any, next=None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node with value {self.value}"


class SinglyNode(AbstractNode):
    def __init__(self, value: Any, next=None) -> None:
        self.value = value
        self.next = next


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
        if self.head is None:
            self.head = node
        else:
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

    def _increment(self, base: int = 1) -> None:
        self.len += base

    def _decrement(self, base: int = 1) -> None:
        self.len -= base

    def _del(self, prevNode: SinglyNode) -> SinglyNode:
        if prevNode is None:
            self.head = self.head.next
            self._decrement()
            return self.head
        else:
            nextNode = prevNode.next
            prevNode.next = nextNode.next if nextNode else None
            self._decrement()
            return prevNode.next

    def _count_len(self, otherSLL: AbstractSinglyListNode) -> int:
        counter = 0
        tail = None
        node = otherSLL.head
        while node:
            counter += 1
            tail = node
            node = node.next
        return counter, tail

    def add_head(self, node: Union[SinglyNode, Any]):
        node = self._nodify(node)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self._increment()

    def add_back(self, node: Union[SinglyNode, Any]) -> None:
        """This method return the Error if in the ListNode there isn't head"""
        node = self._nodify(node)
        self.tail.next = node
        self.tail = self.tail.next
        self._increment()

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
            self._increment()

    def merge(self, otherSLL: AbstractSinglyListNode) -> None:
        if self.head is None:
            other_len = 0
            if isinstance(otherSLL, self.__class__):
                other_len = otherSLL.len
                other_tail = otherSLL.tail
            else:
                other_len, other_tail = self._count_len(otherSLL)
            self.head = otherSLL.head
            self.tail = other_tail
            self._increment(other_len)

        else:
            other_len = 0
            if isinstance(otherSLL, self.__class__):
                other_len = otherSLL.len
                other_tail = otherSLL.tail
            else:
                other_len, other_tail = self._count_len(otherSLL)

            self.tail.next = otherSLL.head
            self.tail = other_tail
            self._increment(other_len)


class DoublyNode(AbstractNode):
    def __init__(
        self,
        value: Union[int, SinglyNode],
        next=None,
        prev=None,
    ) -> None:
        self.next = next
        self.prev = prev

        if isinstance(value, SinglyNode):
            self.value = value.value
        else:
            self.value = value


class AdvancedDoublyListNode(AdvancedSinglyListNode):
    def __init__(self, head_node: Union[DoublyNode, Any] = None) -> None:
        self.head: DoublyNode = None
        self.tail: DoublyNode = None
        self.len = 0

        if head_node != None:
            self.add_head(head_node)
            self.tail = self.head

    def _nodify(self, entity: Any) -> DoublyNode:
        if isinstance(entity, DoublyNode):
            return entity
        return DoublyNode(entity)

    def _forward_backward(self, position: int) -> int:
        if position >= 0:
            forward_paces = position
            backward_paces = self.len - position
        else:
            forward_paces = self.len + position
            backward_paces = abs(position)

        return forward_paces, backward_paces

    def _ftrav(self, paces: int) -> DoublyNode:
        node = self.head
        for _ in range(paces):
            node = node.next
        return node

    def _btrav(self, paces: int) -> DoublyNode:
        node = self.tail
        for _ in range(paces - 1):
            node = node.prev
        return node

    def _del(self, prevNode: DoublyNode) -> DoublyNode:
        if prevNode is None:
            self.head = self.head.next
            self._decrement()
            return self.head
        else:
            nextNode = prevNode.next
            prevNode.next = nextNode.next if nextNode else None
            self._decrement()
            return prevNode.next

    def add_head(self, node: Union[DoublyNode, Any]):
        node = self._nodify(node)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self._increment()

    def add_back(self, node: Union[DoublyNode, Any]) -> None:
        node = self._nodify(node)
        prev = self.tail

        self.tail.next = node
        self.tail = self.tail.next
        self.tail.prev = prev

        self._increment()

    def _traversal(self, position: int) -> DoublyNode:
        forward_paces, backward_paces = self._forward_backward(position)
        forward = True if forward_paces <= backward_paces else False
        paces = min(forward_paces, backward_paces)

        node = self._ftrav(paces) if forward else self._btrav(paces)
        return node

    def find(self, position: int) -> SinglyNode:
        if (position >= self.len) or (position < 0 and position < -self.len):
            raise ValueError("Position > len(ListNode)")
        elif (position == self.len - 1) or (position == -1):
            return self.tail
        elif (position == 0) or (position == -self.len):
            return self.head
        else:
            return self._traversal(position)

    def delpos(
        self,
        position: int = None,
    ) -> SinglyNode:
        position = position - 1 if position >= 0 else position + 1
        prevNode = self.find(position)
        node = self._del(prevNode)
        return node


def test_SLL():
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

    assl.reverse()
    print(assl)


if __name__ == "__main__":
    massive = [0, 1, 2, 3, 4, 5]

    dll = AdvancedDoublyListNode()
    dll.from_list(massive)

    # node1 = DoublyNode(1)
    # node2 = DoublyNode(2)
    # node3 = DoublyNode(3)

    # dll.add_head(node1)
    # dll.add_back(node2)
    # dll.add_back(node3)

    print(dll.find(2))
