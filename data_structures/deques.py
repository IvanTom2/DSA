from abc import abstractmethod
from arrays import DynamicArray
from linked_list import AdvancedSinglyLinkedList, AdvancedDoublyLinkedList


class DequeInterface(object):
    def __init__(self) -> None:
        self._storage = self._get_storage()

    @abstractmethod
    def _get_storage(self):
        return []

    def push_front(self, value: int) -> None:
        self._storage.insert(0, value)

    def push_back(self, value: int) -> None:
        self._storage.append(value)

    def pop_front(self) -> int:
        return self._storage.pop(0)

    def pop_back(self) -> int:
        return self._storage.pop()

    def __len__(self) -> int:
        return len(self._storage)

    def isEmpty(self):
        return len(self) == 0

    def __repr__(self) -> str:
        return f"{self._storage}"

    def to_list(self) -> list[int]:
        return self._storage


class ListDeque(DequeInterface):
    def _get_storage(self):
        return []


class DynamicArrayDeque(DequeInterface):
    def _get_storage(self):
        self._storage: DynamicArray
        return DynamicArray()

    def push_front(self, value: int) -> None:
        self._storage.insert(value, 0)

    def pop_front(self) -> int:
        return self._storage.remove(0)

    def to_list(self) -> list[int]:
        return self._storage.to_list()


class SLLDeque(DynamicArrayDeque):
    def _get_storage(self):
        return AdvancedSinglyLinkedList()


class DLLDeque(DynamicArrayDeque):
    def _get_storage(self):
        return AdvancedDoublyLinkedList()


if __name__ == "__main__":
    deque = ListDeque()
    values = [1, 2, 3, 4]

    for value in values:
        deque.push_back(value)

    while not deque.isEmpty():
        print(deque.pop_back())
