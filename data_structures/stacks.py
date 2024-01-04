from arrays import StaticArray, DynamicArray
from linked_list import AdvancedSinglyLinkedList, AdvancedDoublyLinkedList


class ListStack(object):
    def __init__(self) -> None:
        self._storage = []

    def push(self, value: int) -> None:
        self._storage.append(value)

    def pop(self) -> int:
        return self._storage.pop()

    def peek(self) -> int:
        return self._storage[self.__len__() - 1]

    def __len__(self) -> int:
        return len(self._storage)

    def isEmpty(self) -> bool:
        return len(self._storage) == 0

    def __repr__(self) -> str:
        return f"{self._storage}"

    def to_list(self) -> list[int]:
        return self._storage


class StaticArrayStack(ListStack):
    def __init__(self) -> None:
        self._storage = StaticArray()

    def to_list(self) -> list[int]:
        return self._storage.to_list()


class DynamicArrayStack(StaticArrayStack):
    def __init__(self) -> None:
        self._storage = DynamicArray()


class SinglyLinkedListStack(ListStack):
    def __init__(self) -> None:
        self._storage = AdvancedSinglyLinkedList()

    def to_list(self) -> list[int]:
        return self._storage.to_list()


class DoublyLinkedListStack(SinglyLinkedListStack):
    def __init__(self) -> None:
        self._storage = DoublyLinkedListStack()
