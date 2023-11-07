class SinglyNode(object):
    def __init__(self, value: int, next=None) -> None:
        self.value = value
        self.next = next


class SinglyListNode(object):
    def __init__(self, head_value: SinglyNode = None) -> None:
        self.head: SinglyNode = None
        self.tail: SinglyNode = None
        self.cur_node: SinglyNode = None
        self.len = 0

        if head_value != None:
            self.add_head(head_value)

    def __increment(self):
        self.len += 1

    def __decrement(self):
        self.len -= 1

    def add_head(self, value: int) -> None:
        """Adding node at the head if the head not exists"""
        if self.head:
            raise ValueError("Head node exists")

        self.head = SinglyNode(value)
        self.tail = self.head
        self.__increment()

    def add(self, value: int) -> None:
        """Adding node at the tail of ListNode"""
        node = SinglyNode(value)
        self.tail.next = node
        self.tail = node
        self.__increment()

    def find(self, position: int) -> SinglyNode:
        node = self.head
        while position:
            node = node.next
            position -= 1
        return node

    def insert_by_position(self, value: int, position: int) -> None:
        """
        Insert node at the position.
        To insert node at the head use 0.
        To insert node at the tail use -1.
        """
        if position == 0:
            oldHead = self.head
            self.head = SinglyNode(value)
            self.head.next = oldHead

        elif position == -1 or position == self.len:
            self.add(value)

        else:
            if position > self.len:
                raise ValueError("Position > maxlen of ListNode")

            prevNode = self.find(position - 1)
            nextNode = prevNode.next

            node = SinglyNode(value)
            prevNode.next = node
            node.next = nextNode

    def delete_by_position(
        self,
        position: int,
        _return: bool = False,
    ) -> None:
        """
        Delete node by position.
        To delete node at the head use 0.
        To delete node at the tail use -1.
        """
        if position > self.len:
            raise ValueError("Position > maxlen of ListNode")

        if position == 0:
            node = self.head
            self.head = node.next

        elif position == -1 or position == self.len:
            node = self.tail
            prev = self.find(self.len - 2)
            self.tail = prev
            self.tail.next = None

        else:
            prev = self.find(position - 1)
            node = prev.next
            prev.next = node.next

        self.__decrement()
        if _return:
            return node

    def to_list(self) -> list[SinglyNode]:
        massive = []
        node = self.head
        while node:
            massive.append(node.value)
            node = node.next

        return massive

    def from_list(self, massive: list) -> None:
        start = 0
        if not self.head:
            self.add_head(massive[0])
            start += 1

        for index in range(start, len(massive)):
            self.add(massive[index])

    def __iter__(self):
        self.cur_node = self.head
        return self

    def __next__(self):
        if self.cur_node is None:
            raise StopIteration

        node = self.cur_node
        self.cur_node = self.cur_node.next

        return node

    def __repr__(self):
        return " -> ".join(map(str, self.to_list()))


class DoublyNode(object):
    def __init__(
        self,
        value: int,
        next=None,
        prev=None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyListNode(object):
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    massive = [0, 1, 2, 3, 4, 5]

    listNode = SinglyListNode()
    listNode.from_list(massive)

    print(listNode)

    # listNode.insert_by_position(6, 5)
    listNode.delete_by_position(3)

    print(listNode)

    # node = listNode.find_node(0)
    # for node in listNode:
    #     print(node.value)
