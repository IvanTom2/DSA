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
    reverse_massive: bool = False,
):
    if reverse_massive:
        if isinstance(massive, list):
            massive.reverse()
        else:
            massive = list(massive)
            massive.reverse()

    mList = map(lambda x: x.value, listNode)
    result = map(lambda x: x[0] - x[1], zip(mList, massive))
    assert set(result) == set([0])


def add_head_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    for adds in range(1, 6):
        listNode: ClassicSinglyListNode = listNodeClass()
        for add in range(1, adds):
            listNode.add_head(SinglyNode(add))
            compare_to_list(
                listNode,
                range(1, add + 1),
                reverse_massive=True,
            )


def add_back_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    for adds in range(1, 6):
        listNode: ClassicSinglyListNode = listNodeClass()
        for add in range(1, adds):
            listNode.add_back(SinglyNode(add))
            compare_to_list(
                listNode,
                range(1, add + 1),
                reverse_massive=False,
            )


def add_head_back_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.add_head(SinglyNode(0))
    listNode.add_head(SinglyNode(1))
    listNode.add_back(SinglyNode(2))
    listNode.add_back(SinglyNode(3))
    listNode.add_head(SinglyNode(4))
    compare_to_list(listNode, [4, 1, 0, 2, 3])

    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.add_back(SinglyNode(0))
    listNode.add_back(SinglyNode(1))
    listNode.add_back(SinglyNode(2))
    listNode.add_back(SinglyNode(3))
    listNode.add_head(SinglyNode(4))
    compare_to_list(listNode, [4, 0, 1, 2, 3])


def insert_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ],
    nodeClass: Union[
        SinglyNode,
        DoublyNode,
    ],
):
    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.insert(nodeClass(0), 0)
    listNode.insert(nodeClass(1), 0)
    listNode.insert(nodeClass(2), 0)
    listNode.insert(nodeClass(3), 0)
    compare_to_list(listNode, [3, 2, 1, 0])

    listNode.insert(nodeClass(4), 2)
    listNode.insert(nodeClass(5), 4)
    listNode.insert(nodeClass(6), 0)
    listNode.insert(nodeClass(7), 5)

    # print(listNode)

    compare_to_list(listNode, [6, 3, 2, 4, 1, 7, 5, 0])


def find_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    massive = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.from_list(massive)

    nodes = []
    for index in range(len(massive)):
        node = listNode.find(index)
        nodes.append(node)

    nodes = map(lambda x: x.value, nodes)
    result = map(lambda x: x[0] - x[1], zip(nodes, massive))
    assert set(result) == set([0])


def delpos_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    massive = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.from_list(massive)
    [listNode.delpos(0) for _ in range(len(massive))]
    assert not listNode.to_list()

    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.from_list(massive)
    index = len(massive) - 1
    while index >= 0:
        listNode.delpos(index)
        index -= 1
    assert not listNode.to_list()

    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.from_list(massive)
    listNode.delpos(0)
    listNode.delpos(9)
    listNode.delpos(4)
    listNode.delpos(6)

    mList = listNode.to_list()
    result = map(lambda x: x[0] - x[1], zip(mList, [1, 2, 3, 4, 6, 7, 9]))
    assert set(result) == set([0])


def delval_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    def _delval_test(massive: list[int]) -> None:
        listNode: ClassicSinglyListNode = listNodeClass()
        listNode.from_list(massive)
        [listNode.delval(value) for value in massive]
        assert not listNode.to_list()

    massive = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    _delval_test(massive)

    massive = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    _delval_test(massive)

    massive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    _delval_test(massive)


def reverse_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    massive = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listNode: ClassicSinglyListNode = listNodeClass()
    listNode.from_list(massive)

    massive.reverse()
    listNode.reverse()

    assert massive == listNode.to_list()


def merge_tests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ]
):
    massive1 = [0, 1, 2]
    massive2 = [3, 4, 5]
    massive3 = [6, 7, 8]
    massive4 = [9, 10, 11]
    massive5 = [12, 13, 14]
    mTarget = []

    mainNode: ClassicSinglyListNode = listNodeClass()
    listNode1: ClassicSinglyListNode = listNodeClass()
    listNode2: ClassicSinglyListNode = listNodeClass()

    CSLL = ClassicSinglyListNode()
    ASLL = AdvancedSinglyListNode()
    ADLL = AdvancedDoublyListNode()

    listNode1.from_list(massive1)
    listNode2.from_list(massive2)
    CSLL.from_list(massive3)
    ASLL.from_list(massive4)
    ADLL.from_list(massive5)

    mainNode.merge(listNode1)
    mTarget += massive1
    assert mainNode.to_list() == mTarget

    mainNode.merge(listNode2)
    mTarget += massive2
    assert mainNode.to_list() == mTarget

    mainNode.merge(CSLL)
    mTarget += massive3
    assert mainNode.to_list() == mTarget

    mainNode.merge(ASLL)
    mTarget += massive4
    assert mainNode.to_list() == mTarget

    mainNode.merge(ADLL)
    mTarget += massive5
    assert mainNode.to_list() == mTarget


def listNodeTests(
    listNodeClass: Union[
        ClassicSinglyListNode,
        AdvancedSinglyListNode,
        AdvancedDoublyListNode,
    ],
    nodeClass: Union[
        SinglyNode,
        DoublyNode,
    ],
) -> None:
    add_head_tests(listNodeClass)
    add_back_tests(listNodeClass)
    add_head_back_tests(listNodeClass)
    find_tests(listNodeClass)
    insert_tests(listNodeClass, nodeClass)
    delpos_tests(listNodeClass)
    delval_tests(listNodeClass)
    reverse_tests(listNodeClass)
    merge_tests(listNodeClass)


def test_CSLL():
    listNodeTests(ClassicSinglyListNode, SinglyNode)


def test_ASLL():
    listNodeTests(AdvancedSinglyListNode, SinglyNode)


def test_ADLL():
    listNodeTests(AdvancedDoublyListNode, DoublyNode)


raise ValueError("TODO: same tests after merging of LL")

if __name__ == "__main__":
    # test_CSLL()
    # test_ASLL()
    test_ADLL()
