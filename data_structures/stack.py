class ListStack(object):
    def __init__(self) -> None:
        self.__storage = []

    def push(self, value: int) -> None:
        self.__storage.append(value)

    def pop(self) -> int:
        return self.__storage.pop()

    def peek(self) -> int:
        return self.__storage[-1]

    def __len__(self) -> int:
        return len(self.__storage)

    def isEmpty(self) -> bool:
        return len(self.__storage) == 0

    def __repr__(self) -> str:
        return f"{self.__storage}"


if __name__ == "__main__":
    stack = ListStack()

    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack)
