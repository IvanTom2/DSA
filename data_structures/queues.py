import random
from abc import abstractmethod
from arrays import StaticArray
from time_measure import repeater

from arrays import StaticArray, DynamicArray
from linked_list import AdvancedSinglyLinkedList, AdvancedDoublyLinkedList


class QueueInterface(object):
    def __init__(self) -> None:
        self._storage = self._get_storage()

    @abstractmethod
    def _get_storage(self):
        return []

    def enqueue(self, value: int) -> None:
        self._storage.append(value)

    def dequeue(self) -> int:
        return self._storage.pop(0)

    def peek(self) -> int:
        return self._storage[0]

    def __len__(self) -> int:
        return len(self._storage)

    def isEmpty(self) -> bool:
        return len(self._storage) == 0

    def to_list(self) -> list[int]:
        return self._storage

    def __repr__(self) -> str:
        return f"{self._storage}"


class LazyQueueInterface(QueueInterface):
    def __init__(self) -> None:
        super().__init__()
        self._head = 0

    def _reallocate(self):
        self._storage = self._storage[self._head :]
        self._head = 0

    def peek(self) -> int:
        return self._storage[self._head]

    def dequeue(self) -> int:
        value = self.peek()
        self._head += 1

        if self._head > len(self._storage) // 2:
            self._reallocate()

        return value

    def __len__(self) -> int:
        return len(self._storage) - self._head


class ListQueue(QueueInterface):
    def __init__(self) -> None:
        super().__init__()


class StaticArrayQueue(QueueInterface):
    def __init__(self) -> None:
        super().__init__()
        self._storage: StaticArray

    def _get_storage(self) -> StaticArray:
        return StaticArray()

    def dequeue(self) -> int:
        return self._storage.remove(0)

    def to_list(self) -> list[int]:
        return self._storage.to_list()


class DynamicArrayQueue(StaticArrayQueue):
    def __init__(self) -> None:
        super().__init__()

    def _get_storage(self) -> DynamicArray:
        return DynamicArray()


class SLLQueue(QueueInterface):
    def __init__(self) -> None:
        super().__init__()
        self._storage: AdvancedSinglyLinkedList

    def _get_storage(self):
        return AdvancedSinglyLinkedList()

    def dequeue(self) -> int:
        return self._storage.remove(0)

    def to_list(self) -> list[int]:
        return self._storage.to_list()


class DLLQueue(SLLQueue):
    def __init__(self) -> None:
        super().__init__()

    def _get_storage(self):
        return AdvancedDoublyLinkedList()


class ListLazyQueue(LazyQueueInterface):
    def __init__(self) -> None:
        super().__init__()

    def _get_storage(self):
        return []


class DynamicArrayLazyQueue(LazyQueueInterface):
    def __init__(self) -> None:
        super().__init__()

    def _get_storage(self):
        return DynamicArray()

    def _reallocate(self):
        size = len(self._storage)
        old_storage = self._storage
        self._storage = self._get_storage()

        while self._head < size:
            self.enqueue(old_storage[self._head])
            self._head += 1

        self._head = 0


class SLLLazyQueue(DynamicArrayLazyQueue):
    def __init__(self) -> None:
        super().__init__()

    def _get_storage(self):
        return AdvancedSinglyLinkedList()


class DLLLazyQueue(DynamicArrayLazyQueue):
    def __init__(self) -> None:
        super().__init__()

    def _get_storage(self):
        return AdvancedDoublyLinkedList()


@repeater()
def do_benchmark(n: int, queue_class: ListQueue) -> None:
    queue: ListQueue = queue_class()
    for num in range(n):
        queue.enqueue(num)

    while not queue.isEmpty():
        queue.dequeue()

    for num in range(n):
        if random.random() >= 0.5:
            if not queue.isEmpty():
                queue.dequeue()
        else:
            queue.enqueue(num)


if __name__ == "__main__":
    # n = 100

    # do_benchmark(n, ListQueue)
    # do_benchmark(n, ListLazyQueue)
    # do_benchmark(n, DynamicArrayQueue)
    # do_benchmark(n, SLLQueue)
    # do_benchmark(n, DLLQueue)

    queue = DynamicArrayLazyQueue()
    for num in range(10):
        queue.enqueue(num)

    while not queue.isEmpty():
        print(queue.dequeue())
