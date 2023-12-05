class MemoryCell(object):
    def __init__(self, value: int) -> None:
        self.__value = value

    def assign(self, value: int) -> None:
        self.__value = value

    def get(self) -> int:
        return self.__value

    def __repr__(self) -> str:
        return f"{self.get()}"


class NotAllowedMemoryCell(MemoryCell):
    def __init__(self) -> None:
        self.__value = "_"

    def assign(self, value: int) -> None:
        raise MemoryError("Assign Segmentation Fault")

    def get(self) -> None:
        raise MemoryError("Get Segmentation Fault")

    def __repr__(self) -> str:
        return self.__value


class Memory(object):
    def __init__(self, size: int, large: int = 4) -> None:
        self._size = size

        self.storage = [NotAllowedMemoryCell() for _ in range(size * large)]

    def access(self, subsript: int) -> MemoryCell:
        return self.storage[subsript]

    def allocate(self) -> int:
        low_bound = round((len(self.storage) - self._size) / 2)
        self.storage[low_bound : low_bound + self._size] = [
            MemoryCell("E") for _ in range(self._size)
        ]
        return low_bound

    def __repr__(self) -> str:
        return f"{self.storage}"


if __name__ == "__main__":
    mem = Memory(4, 4)
    mem.allocate()

    print(mem.storage)
