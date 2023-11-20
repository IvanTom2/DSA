import random
from copy import copy


class MemoryCell(object):
    def __init__(self, value: int) -> None:
        self.__value = value

    def assign(self, value: int) -> None:
        self.__value = value

    def get(self) -> int:
        return self.__value

    def __repr__(self) -> str:
        return f"{self.get()}"


class Memory(object):
    def __init__(self, size: int) -> None:
        self._size = size
        self.storage = [MemoryCell(0) for _ in range(size * 4)]

    def access(self, subsript: int) -> MemoryCell:
        return self.storage[subsript]

    def allocate(self) -> int:
        low_bound = round(len(self.storage) / 2)
        self.storage[low_bound : low_bound + self._size] = [
            MemoryCell(None) for _ in range(self._size)
        ]
        return low_bound

    def __repr__(self) -> str:
        return f"{self.storage}"


class Array(object):
    def __init__(self, size: int) -> None:
        self.memory: Memory
        self.low_bound: int
        self.size = 1 if not size else size
        self.count = 0

        self.__allocate_memory(size)

    def __allocate_memory(self, size: int) -> list[int]:
        self.memory = Memory(size)
        self.low_bound = self.memory.allocate()
        self.high_bound = self.low_bound + self.size

    def _index_pcheck(self, index: int):
        if index > self.size - 1:
            raise IndexError()

    def _index_ncheck(self, index: int):
        if index < 0:
            raise IndexError()

    def _index_checkout(self, index: int):
        self._index_ncheck(index)
        self._index_pcheck(index)

    def _access(self, index: int) -> MemoryCell:
        subscript = self.low_bound + index
        return self.memory.access(subscript)

    def _shift_right(self, index: int) -> None:
        if self.low_bound + self.count < self.high_bound:
            indexer = self.size - 1
            while indexer > index:
                value = self._access(indexer - 1).get()
                self.replace(value, indexer)
                indexer -= 1

            self.replace(None, index)

        else:
            raise IndexError()

    def _shift_left(self, index: int) -> None:
        for indexer in range(index, self.size - 1):
            value = self._access(indexer + 1).get()
            self.replace(value, indexer)
        self.replace(None, self.size - 1)

    def push(self, value: int) -> None:
        self._index_checkout(self.count)
        self.replace(value, self.count)
        self.count += 1

    def replace(self, value: int, index: int) -> None:
        memory_cell = self._access(index)
        memory_cell.assign(value)

    def insert(self, value: int, index: int) -> None:
        self._index_checkout(index)
        self._shift_right(index)
        self.replace(value, index)
        self.count += 1

    def remove(self, index) -> int:
        self._index_checkout(index)
        returning_value = self._access(index).get()
        self._shift_left(index)
        self.count -= 1

        return returning_value

    def pop(self) -> int:
        self._index_checkout(self.count - 1)
        returning_value = self._access(self.count - 1).get()
        self.replace(None, self.count - 1)
        self.count -= 1

        return returning_value

    @property
    def values(self) -> list[int]:
        return [self._access(i) for i in range(0, self.size)]

    def __repr__(self) -> str:
        return f"{self.values}"


class DynamicArray(Array):
    def __init__(self, size: int, dynamic: int = 2) -> None:
        super().__init__(size)
        self._dynamic = dynamic

    def __reallocate_memory(self):
        tempo = self.values
        self.size = self.size * self._dynamic
        self.count = 0

        self.memory = Memory(self.size)
        self.low_bound = self.memory.allocate()
        self.high_bound = self.low_bound + self.size

        for value in tempo:
            self.push(value)

        del tempo

    def _index_pcheck(self, index: int):
        if index > self.size - 1:
            self.__reallocate_memory()


def fill_array(array: Array, value_list: list[int]) -> None:
    tuple(map(array.push, value_list))


if __name__ == "__main__":
    array = Array(10)
