class ListDeque(object):
    def __init__(self) -> None:
        self.__storage = []

    def addFirst(self, value: int) -> None:
        self.__storage.append(value)

    def addLast(self, value: int) -> None:
        self.__storage.insert(0, value)

    def getFirst(self) -> int:
        self.__storage.pop(0)

    def getLast(self) -> int:
        self.__storage.pop()

    def __len__(self) -> int:
        return len(self.__storage)

    def __repr__(self) -> str:
        return f"{self.__storage}"


if __name__ == "__main__":
    deque = ListDeque()

    deque.addFirst(0)
    deque.addLast(1)
    deque.addFirst(2)
    deque.addLast(3)

    print(deque)
