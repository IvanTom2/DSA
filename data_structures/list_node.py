from abc import ABC
from typing import Any, Union
from functools import wraps


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


class AbstractSinglyListNode(ABC):
    def __init__(self, head: SinglyNode = None) -> None:
        self.head: SinglyNode = head


class AbstractDoublyListNode(ABC):
    def __init__(self, head: DoublyNode = None) -> None:
        self.head: DoublyNode = head


class ClassicSinglyListNode(AbstractSinglyListNode):
    """Classical SLL (Singly Linked List)"""

    def __init__(self, head_node: Union[SinglyNode, Any] = None) -> None:
        self.head: SinglyNode = None

        if head_node:
            self.head = self.add_head(head_node)

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

    def _find_tail(self) -> SinglyNode:
        tail = self.head
        if tail:
            while tail.next:
                tail = tail.next
        return tail

    def _check_class(self, otherSLL: AbstractSinglyListNode) -> None:
        if isinstance(otherSLL, AbstractSinglyListNode):
            if isinstance(otherSLL, AbstractDoublyListNode):
                raise ValueError("Can't merge singly and doubly linked lists")
        else:
            raise ValueError(f"Can't merge singly linked list and {otherSLL.__class__}")

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

        if self.head is None:
            self.head = node
        else:
            tail = self._find_tail()
            tail.next = node

    def _insert(self, node: Union[SinglyNode, Any], position: int) -> None:
        node = self._nodify(node)

        prevNode = self.find(position - 1)
        nextNode = prevNode.next

        prevNode.next = node
        node.next = nextNode

    def insert(
        self,
        node: Union[SinglyNode, Any],
        position: int,
    ) -> None:
        if position == 0:
            self.add_head(node)
        else:
            self._insert(node, position)

    def delpos(
        self,
        position: int = None,
    ) -> SinglyNode:
        if position == 0:
            oldHead = self.head
            self.head = oldHead.next
            return oldHead
        else:
            prevNode = self.find(position - 1)
            self._del(prevNode)
            return prevNode

    def delval(
        self,
        node: Union[SinglyNode, Any],
        maxdel: int = 0,
    ) -> None:
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

    def reverse(self) -> None:
        prev = None
        node = self.head

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

        self.head = prev

    def merge(self, otherSLL: AbstractSinglyListNode) -> None:
        self._check_class(otherSLL)

        if self.head is None:
            self.head = otherSLL.head

        else:
            tail = self._find_tail()
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

    def __next__(self) -> SinglyNode:
        if self.cur_node is None:
            raise StopIteration

        node = self.cur_node
        self.cur_node = self.cur_node.next

        return node

    def __repr__(self) -> str:
        return " -> ".join(map(str, self.to_list()))


class AdvancedSinglyListNode(ClassicSinglyListNode):
    def __init__(self, head_node: Union[SinglyNode, Any] = None) -> None:
        self.head: SinglyNode = None
        self.tail: SinglyNode = None
        self.len = 0

        if head_node is not None:
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
            nextNode: SinglyNode = prevNode.next
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
        if self.tail is None:
            self.add_head(node)
        else:
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

    def _insert(
        self,
        node: Union[SinglyNode, Any],
        position: int,
    ) -> None:
        node = self._nodify(node)

        prevNode = self.find(position - 1)
        nextNode = prevNode.next

        prevNode.next = node
        node.next = nextNode
        self._increment()

    def merge(self, otherSLL: AbstractSinglyListNode) -> None:
        self._check_class(otherSLL)

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


class AdvancedDoublyListNode(AdvancedSinglyListNode, AbstractDoublyListNode):
    def __init__(self, head_node: Union[DoublyNode, Any] = None) -> None:
        self.head: DoublyNode = None
        self.tail: DoublyNode = None
        self.len = 0

        if head_node is not None:
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
        for _ in range(paces):
            node = node.prev
        return node

    def _del(self, prevNode: DoublyNode) -> DoublyNode:
        if prevNode is None:
            oldHead = self.head
            self.head = oldHead.next
            self._decrement()
            return self.head
        else:
            curNode: DoublyNode = prevNode.next
            nextNode: DoublyNode = curNode.next if curNode else None

            prevNode.next = nextNode
            if nextNode is not None:
                nextNode.prev = prevNode

            self._decrement()
            return nextNode

    def _check_class(self, otherDLL: AbstractDoublyListNode) -> None:
        if isinstance(otherDLL, AbstractDoublyListNode):
            pass
        else:
            raise ValueError(f"Can't merge singly linked list and {otherDLL.__class__}")

    def add_head(self, node: Union[DoublyNode, Any]) -> None:
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
        if self.tail is None:
            self.add_head(node)
        else:
            prev = self.tail

            self.tail.next = node
            self.tail = self.tail.next
            self.tail.prev = prev

        self._increment()

    def _traversal(self, position: int) -> DoublyNode:
        forward_paces, backward_paces = self._forward_backward(position)
        forward = True if forward_paces <= backward_paces else False
        paces = min(forward_paces, backward_paces)

        node = self._ftrav(paces) if forward else self._btrav(paces - 1)
        return node

    def find(self, position: int) -> DoublyNode:
        if (position >= self.len) or (position < 0 and position < -self.len):
            raise ValueError("Position > len(ListNode)")
        elif (position == self.len - 1) or (position == -1):
            return self.tail
        elif (position == 0) or (position == -self.len):
            return self.head
        else:
            return self._traversal(position)

    def _insert(
        self,
        node: Union[DoublyNode, Any],
        position: int,
    ) -> None:
        node = self._nodify(node)

        prevNode: DoublyNode = self.find(position - 1)
        nextNode: DoublyNode = prevNode.next

        prevNode.next = node
        nextNode.prev = node

        node.next = nextNode
        node.prev = prevNode

        self._increment()

    def delpos(
        self,
        position: int = None,
    ) -> SinglyNode:
        if (position >= self.len) or (position < 0 and position < -self.len):
            raise ValueError("Position > len(ListNode)")

        elif (position == 0) or (position == -self.len):
            oldHead = self.head
            nextNode: DoublyNode = oldHead.next

            if nextNode is not None:
                nextNode.prev = None

            self.head = nextNode
            self._decrement()
            return oldHead

        elif (position == self.len - 1) or (position == -1):
            oldTail = self.tail
            prevNode: DoublyNode = oldTail.prev

            if prevNode is not None:
                prevNode.next = None

            self.tail = prevNode
            self._decrement()
            return oldTail

        else:
            position = position - 1 if position >= 0 else position - 1
            prevNode = self.find(position)

            node = self._del(prevNode)
            return node

    def merge(self, otherDLL: AbstractDoublyListNode) -> None:
        self._check_class(otherDLL)

        if self.head is None:
            other_len = 0
            if isinstance(otherDLL, self.__class__):
                other_len = otherDLL.len
                other_tail = otherDLL.tail
            else:
                other_len, other_tail = self._count_len(otherDLL)
            self.head = otherDLL.head
            self.tail = other_tail
            self._increment(other_len)

        else:
            other_len = 0
            if isinstance(otherDLL, self.__class__):
                other_len = otherDLL.len
                other_tail = otherDLL.tail
            else:
                other_len, other_tail = self._count_len(otherDLL)

            self.tail.next = otherDLL.head
            self.tail = other_tail
            self._increment(other_len)

    def reverse(self) -> None:
        prev = None
        oldHead = self.head
        node = oldHead

        while node:
            next = node.next

            node.next = prev
            node.prev = next

            prev = node
            node = next

        self.head = prev
        self.tail = oldHead


class CircularSinglyListNode(AdvancedSinglyListNode):
    def __init__(self, head_node: Union[SinglyNode, Any] = None) -> None:
        super().__init__(head_node)

    def loop_list(self) -> None:
        self.tail.next = self.head

    def loop_decor(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            output = func(self, *args, **kwargs)
            self.loop_list()
            return output

        return wrapper

    @loop_decor
    def add_back(self, node: SinglyNode | Any) -> None:
        return super().add_back(node)

    @loop_decor
    def add_head(self, node: SinglyNode | Any):
        return super().add_head(node)

    @loop_decor
    def _insert(self, node: SinglyNode | Any, position: int) -> None:
        return super()._insert(node, position)

    @loop_decor
    def merge(self, otherSLL: AbstractSinglyListNode) -> None:
        return super().merge(otherSLL)

    def to_list(self) -> list[SinglyNode]:
        head = self.head
        massive = [head.value]

        node: SinglyNode = self.head.next
        while node and node != head:
            massive.append(node.value)
            node = node.next

        return massive


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

    sll = AdvancedDoublyListNode()

    sll.add_back(0)
    sll.add_back(1)
    sll.add_back(2)
    sll.add_back(3)
    sll.add_back(4)

    sll.reverse()

    print(sll)
    print(sll.head, sll.head.next, sll.head.prev)
    print(sll.tail, sll.tail.next, sll.tail.prev)
