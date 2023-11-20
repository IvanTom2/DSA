class ListQueue(object):
    def __init__(self) -> None:
        self.__storage = []

    def enqueue(self, value: int) -> None:
        self.__storage.append(value)

    def dequeue(self) -> int:
        return self.__storage.pop(0)

    def peek(self) -> int:
        return self.__storage[0]

    def __len__(self) -> int:
        return len(self.__storage)

    def isEmpty(self) -> bool:
        return len(self.__storage) == 0

    def __repr__(self) -> str:
        return f"{self.__storage}"


class LazyQueue(ListQueue):
    def __init__(self) -> None:
        super().__init__()
        self.__head = 0

    def dequeue(self) -> int:
        value = self.peek()
        self.__head += 1
        if self.__head > len(self.__storage) // 2:
            self.__storage = self.__storage[self.__head :]
            self.__head = 0

        return value

    def __len__(self) -> int:
        return len(self.__storage) - self.__head


if __name__ == "__main__":
    queue = ListQueue()

    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue)
