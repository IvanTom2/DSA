import sys
from pathlib import Path
from typing import Union
from functools import reduce


sys.path.append(str(Path(__file__).parent.parent))
from list_node import (
    AbstractSinglyListNode,
    ClassicSinglyListNode,
    AdvancedSinglyListNode,
    AdvancedDoublyListNode,
    SinglyNode,
    DoublyNode,
)


def compare_to_list(
    listNode: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ],
    massive: list,
):
    mList = map(lambda x: x.value, listNode)
    result = sum(map(lambda x: x[0] - x[1], zip(mList, massive)))
    assert result == 0


def add_head_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    # listNode: ClassicSinglyListNode = listNodeClass()
    for adds in range(1, 6):
        listNode: ClassicSinglyListNode = listNodeClass()
        for add in adds:
            listNode.add_head(SinglyNode(add))
            compare_to_list(listNode, range(1, add))


def listNodeTests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
) -> None:
    massive = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.add_head(SinglyNode(11))
    compare_to_list(listNode, [11])

    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.add_back(SinglyNode(11))
    compare_to_list(listNode, [11])

    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.add_head(SinglyNode(0))
    listNode.add_head(SinglyNode(1))
    listNode.add_back(SinglyNode(2))
    listNode.add_back(SinglyNode(3))
    listNode.add_head(SinglyNode(4))
    compare_to_list(listNode, [4, 1, 0, 2, 3])

    # print(listNode.to_list())


def test_CSLL():
    listNodeTests(ClassicSinglyListNode)


if __name__ == "__main__":
    test_CSLL()
