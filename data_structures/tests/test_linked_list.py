import sys
import pytest
import random
from pathlib import Path


sys.path.append(str(Path(__file__).parent.parent))
from linked_list import (
    ClassicSinglyLinkedList,
    AdvancedSinglyLinkedList,
    AdvancedDoublyLinkedList,
    SinglyNode,
)


class BaseLinkedListTest(object):
    @pytest.fixture
    def linked_list_cls(self) -> ClassicSinglyLinkedList:
        return ClassicSinglyLinkedList

    @pytest.fixture
    def test_values(self):
        return list(range(4))

    def test_add_head(self, linked_list_cls, test_values: list[int]):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()

        for value in test_values:
            linked_list.add_head(SinglyNode(value))

        test_values.reverse()
        assert linked_list.to_list() == test_values

    def test_push(self, linked_list_cls, test_values: list[int]):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()

        for value in test_values:
            linked_list.push(SinglyNode(value))

        assert linked_list.to_list() == test_values

    def test_add_head_push(self, linked_list_cls, test_values: list[int]):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()

        compare_list = []
        for value in test_values:
            mode = random.random()
            if mode >= 0.5:
                linked_list.push(value)
                compare_list.append(value)
            else:
                linked_list.add_head(value)
                compare_list.insert(0, value)

        assert linked_list.to_list() == compare_list

    def test_forward_full_insert(self, linked_list_cls, test_values: list[int]):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()

        for value in test_values:
            linked_list.insert(value, 0)

        test_values.reverse()
        assert linked_list.to_list() == test_values

    def test_forward_insert(self, linked_list_cls, test_values: list[int]):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()

        for value in test_values[:-1]:
            linked_list.push(value)

        linked_list.insert(test_values[-1], 0)
        assert linked_list.to_list() == [test_values[-1]] + test_values[:-1]

    def test_find(self, linked_list_cls, test_values):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()
        linked_list.from_list(test_values)

        for index in range(len(test_values)):
            node: SinglyNode = linked_list.find_node(index)
            value = node.value
            assert value == test_values[index]

    def test_remove(self, linked_list_cls, test_values):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()
        linked_list.from_list(test_values)
        [linked_list.remove(0) for _ in range(len(test_values))]
        assert len(linked_list.to_list()) == 0

        linked_list: ClassicSinglyLinkedList = linked_list_cls()
        linked_list.from_list(test_values)
        index = len(test_values) - 1
        while index >= 0:
            linked_list.remove(index)
            index -= 1
        assert len(linked_list.to_list()) == 0

    def test_random_remove(self, linked_list_cls, test_values: list[int]):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()
        linked_list.from_list(test_values)

        indexes_to_del = random.sample(
            range(len(test_values) - 1),
            len(test_values) // 2,
        )

        for index in indexes_to_del:
            test_values.pop(index)
            linked_list.remove(index)

            assert linked_list.to_list() == test_values

    def test_delval(self, linked_list_cls, test_values):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()
        linked_list.from_list(test_values)
        [linked_list.remove_value(value) for value in test_values]
        assert len(linked_list.to_list()) == 0

    def test_random_delval(self, linked_list_cls, test_values: list[int]):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()
        linked_list.from_list(test_values)

        values = random.sample(test_values, len(test_values) // 2)
        for value in values:
            test_values.remove(value)
            linked_list.remove_value(value, 1)

        assert linked_list.to_list() == test_values

    def test_reverse(self, linked_list_cls, test_values: list[int]):
        linked_list: ClassicSinglyLinkedList = linked_list_cls()
        linked_list.from_list(test_values)

        test_values.reverse()
        linked_list.reverse()

        assert test_values == linked_list.to_list()

    def test_merge(self, linked_list_cls):
        massive1 = [0, 1, 2]
        massive2 = [3, 4, 5]
        massive3 = [6, 7, 8]
        massive4 = [9, 10, 11]
        mTarget = []

        main_linked_list: ClassicSinglyLinkedList = linked_list_cls()
        linked_list1: ClassicSinglyLinkedList = linked_list_cls()
        linked_list2: ClassicSinglyLinkedList = linked_list_cls()

        CSLL = ClassicSinglyLinkedList()
        ASLL = AdvancedSinglyLinkedList()

        linked_list1.from_list(massive1)
        linked_list2.from_list(massive2)
        CSLL.from_list(massive3)
        ASLL.from_list(massive4)

        main_linked_list.merge(linked_list1)
        mTarget += massive1
        assert main_linked_list.to_list() == mTarget

        main_linked_list.merge(linked_list2)
        mTarget += massive2
        assert main_linked_list.to_list() == mTarget

        main_linked_list.merge(CSLL)
        mTarget += massive3
        assert main_linked_list.to_list() == mTarget

        main_linked_list.merge(ASLL)
        mTarget += massive4
        assert main_linked_list.to_list() == mTarget


class TestClassicLinkedList(BaseLinkedListTest):
    @pytest.fixture
    def linked_list_cls(self) -> ClassicSinglyLinkedList:
        return ClassicSinglyLinkedList


class TestAdvancedLinkedList(BaseLinkedListTest):
    @pytest.fixture
    def linked_list_cls(self) -> AdvancedSinglyLinkedList:
        return AdvancedSinglyLinkedList


class TestDoublyLinkedList(BaseLinkedListTest):
    @pytest.fixture
    def linked_list_cls(self) -> AdvancedDoublyLinkedList:
        return AdvancedDoublyLinkedList

    def test_merge(self, linked_list_cls):
        massive1 = [0, 1, 2]
        massive2 = [3, 4, 5]
        mTarget = []

        mainNode: AdvancedDoublyLinkedList = linked_list_cls()
        listNode1: AdvancedDoublyLinkedList = linked_list_cls()
        listNode2: AdvancedDoublyLinkedList = linked_list_cls()

        listNode1.from_list(massive1)
        listNode2.from_list(massive2)

        mainNode.merge(listNode1)
        mTarget += massive1
        assert mainNode.to_list() == mTarget

        mainNode.merge(listNode2)
        mTarget += massive2
        assert mainNode.to_list() == mTarget
