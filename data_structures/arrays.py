from functools import wraps
from typing import Union
from memory_model import Memory, MemoryCell

from _base import ListInterface


class StaticArray(ListInterface):
    """Array based on modeled class of Memory"""

    def __init__(self, size: int = 4) -> None:
        # next variables from self.__allocate_memory()
        self.memory: Memory
        self.low_bound: int
        self.high_bound: int

        self.size = 1 if not size else size  # max size of array
        self.count = 0  # current size of array

        self.__allocate_memory(size)

    def __allocate_memory(self, size: int) -> list[int]:
        """Memory allocation in modeled class of Memory"""

        self.memory = Memory(size)
        self.low_bound = self.memory.allocate()
        self.high_bound = self.low_bound + self.size

    def _size_check_func(self) -> None:
        """Function used in '_size_check' decorator"""

        if self.count >= self.size:
            raise OverflowError("Array overflow")

    def _size_check(func) -> callable:
        """Array size check decorator"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            arr: StaticArray = args[0]
            arr._size_check_func()
            return func(*args, **kwargs)

        return wrapper

    def _index_checkout(self, index: int) -> None:
        """Index value checkout"""

        if not isinstance(index, int):
            raise IndexError("Index should be integer")
        if index < 0 or index > self.count or index >= self.size:
            raise IndexError("Index out of bound")

    def _access(self, index: int) -> MemoryCell:
        """Access memory cell from modeled class of Memory"""

        subscript = self.low_bound + index
        return self.memory.access(subscript)

    def _memory_assignment(self, value: int, index: int) -> None:
        """Assing new value in memory cell"""

        memory_cell = self._access(index)
        memory_cell.assign(value)

    def _right_shift(self, index: int) -> None:
        # we should check possibility of shifting right
        # without overflow
        self._index_checkout(self.count)

        indexer = self.size - 1
        while indexer > index:
            value = self._access(indexer - 1).get()
            self._memory_assignment(value, indexer)
            indexer -= 1

        self._memory_assignment(None, index)

    def _left_shift(self, index: int) -> None:
        for indexer in range(index, self.size - 1):
            value = self._access(indexer + 1).get()
            self._memory_assignment(value, indexer)
        self._memory_assignment(None, self.size - 1)

    def replace(self, value: int, index: int) -> None:
        """Replace memory cell value"""

        self._index_checkout(index)
        self._memory_assignment(value, index)

    @_size_check
    def push(self, value: int) -> None:
        """Add value at the end of array"""

        self._memory_assignment(value, self.count)
        self.count += 1

    def append(self, value: int) -> None:
        """Add value at the end of array. Same as 'push'"""

        self.push(value)

    @_size_check
    def insert(self, value: int, index: int) -> None:
        """Insert value in specified position of array with right shift"""

        self._index_checkout(index)
        self._right_shift(index)
        self._memory_assignment(value, index)
        self.count += 1

    def pop(self) -> int:
        """Remove and return last value of array"""

        self._index_checkout(self.count - 1)
        returning_value = self._access(self.count - 1).get()
        self._memory_assignment(None, self.count - 1)
        self.count -= 1

        return returning_value

    def get(self, index: int) -> int:
        """Return value by index"""

        self._index_checkout(index)
        return self._access(index).get()

    def remove(self, index: int) -> int:
        """Remove and return value by index"""

        self._index_checkout(self.count - 1)
        returning_value = self.get(index)
        self._left_shift(index)
        self.count -= 1

        return returning_value

    def find(self, value: int) -> int:
        for index in range(0, self.count):
            retrieved = self.get(index)
            if retrieved == value:
                return index

        return None

    def remove_value(self, value: int, n: int = 1) -> list[int]:
        deleted_values = []

        while len(deleted_values) < n:
            index = self.find(value)
            if index is None:
                break

            deleted_values.append(self.remove(index))

        return deleted_values

    def reverse(self) -> None:
        p1, p2 = 0, self.count - 1

        while p1 < p2:
            v1 = self.get(p1)
            v2 = self.get(p2)

            self.replace(v1, p2)
            self.replace(v2, p1)

            p1 += 1
            p2 -= 1

    def merge(self, other_array):
        if isinstance(other_array, self.__class__):
            for value in other_array:
                self.push(value)
        else:
            raise ValueError(f"Can't merge Static Array and {other_array.__class__}")

    def to_list(self) -> list[int]:
        """Return Python List with current values"""
        return [self.get(i) for i in range(0, self.count)]

    def fill_from(self, source: Union[tuple, list]) -> None:
        """Filling array with source values"""

        if isinstance(source, (list, tuple)):
            for value in source:
                self.push(value)
        else:
            NotImplementedError(f"{source.__class__} not implemented for filling")

    def __len__(self) -> int:
        return self.count

    def __getitem__(self, index: int):
        return self.get(index)

    def __setitem__(self, index: int, value: int) -> None:
        self.replace(value, index)

    def __add__(self, other_array):
        self.merge(other_array)
        return self

    def __repr__(self) -> str:
        return f"{[self._access(i) for i in range(0, self.count)]}"


class DynamicArray(StaticArray):
    """Dynamic Array based on modeled class of Memory"""

    def __init__(self, size: int = 4, dynamic_raise: int = 2) -> None:
        super().__init__(size)
        self._dynamic_raise = dynamic_raise

    def __reallocate_memory(self) -> None:
        """Reallocation function special for dynamic array"""

        # print("Start reallocation process")

        tempo_low_bound = self.low_bound
        tempo_high_bound = self.high_bound
        tempo_memory = self.memory

        self.size = self.size * self._dynamic_raise
        self.count = 0
        self.memory = Memory(self.size)

        self.low_bound = self.memory.allocate()
        self.high_bound = self.low_bound + self.size

        for subscript in range(tempo_low_bound, tempo_high_bound):
            value = tempo_memory.access(subscript)
            self.push(value)

        del tempo_low_bound
        del tempo_high_bound
        del tempo_memory

    def _size_check_func(self) -> None:
        if self.count >= self.size:
            self.__reallocate_memory()


class SortedArray(object):
    """Based on Dynamic Array"""

    def __init__(self, size: int, dynamic_raise: int = 2) -> None:
        self._storage = DynamicArray(size, dynamic_raise)

    def _search(self, value: int) -> int:
        """Search insertion index"""

        low, high = 0, self._storage.count
        while low < high:
            mid = low + (high - low) // 2

            if self._storage.get(mid) == value:
                return mid

            if self._storage.get(mid) < value:
                low = mid + 1
            else:
                high = mid

        return low

    def push(self, value: int) -> None:
        """Push value on properly position"""
        if self._storage.count > 0:
            insert_index = self._search(value)
            self._storage.insert(value, insert_index)
        else:
            self._storage.push(value)

    def pop(self) -> None:
        """Remove and return last value of array"""
        return self._storage.pop()

    def __repr__(self) -> str:
        return self._storage.__repr__()
