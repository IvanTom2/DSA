import sys
import random
import pytest
from copy import copy
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from _base import ListInterface
from arrays import StaticArray, DynamicArray
from linked_list import (
    ClassicSinglyLinkedList,
    AdvancedSinglyLinkedList,
    AdvancedDoublyLinkedList,
)


class BaseTestInteface(object):
    @pytest.fixture
    def iclass(self):
        return ListInterface

    @pytest.fixture
    def test_values(self):
        return list(range(4))

    @pytest.fixture
    def cont(self, iclass, test_values):
        if isinstance(iclass, StaticArray):
            cont = iclass(len(test_values))
        else:
            cont = iclass()
        return cont

    @pytest.fixture
    def full_cont(self, cont: ListInterface, test_values):
        for value in test_values:
            cont.push(value)
        return cont

    def test_push_full(self, cont: ListInterface, test_values):
        for value in test_values:
            cont.push(value)

        assert cont.to_list() == test_values

    def test_push_half(self, cont: ListInterface, test_values):
        count = len(test_values) // 2
        for value in test_values[:count]:
            cont.push(value)

        assert cont.to_list() == test_values[:count]

    def test_push_overflow(self, cont: ListInterface, test_values):
        for value in test_values:
            cont.push(value)

        cont.push(100)
        cont.push(200)
        cont.push(300)

        assert cont.to_list() == test_values + [100, 200, 300]

    def test_insert_full_forward(self, cont: ListInterface, test_values: list[int]):
        for value in test_values:
            cont.insert(value, 0)

        test_values.sort(reverse=True)
        assert cont.to_list() == test_values

    def test_insert_full_backward(self, cont: ListInterface, test_values: list[int]):
        for index in range(len(test_values)):
            cont.insert(test_values[index], index)

        assert cont.to_list() == test_values

    def test_insert_after_push(self, cont: ListInterface, test_values: list[int]):
        count = len(test_values) // 2

        for value in test_values[:count]:
            cont.push(value)

        for value in test_values[count:]:
            cont.insert(value, 0)

        v1 = test_values[:count]
        v2 = test_values[count:]
        v2.sort(reverse=True)

        assert cont.to_list() == v2 + v1

    def test_push_insert_random(self, cont: ListInterface, test_values: list[int]):
        compare = []

        for value in test_values:
            mode = random.random()
            if mode >= 0.5 or len(cont) < 1:
                cont.push(value)
                compare.append(value)
            else:
                index = random.randint(0, len(cont) - 1)
                cont.insert(value, index)
                compare.insert(index, value)

        assert cont.to_list() == compare

    def test_pop_full(self, full_cont: ListInterface, test_values: list[int]):
        assert full_cont.to_list() == test_values
        assert len(full_cont) == len(test_values)

        while len(full_cont) > 0:
            test = full_cont.pop()
            comp = test_values.pop()
            assert test == comp

        assert len(full_cont) == 0
        assert len(full_cont) == len(test_values)
        assert full_cont.to_list() == test_values

    def test_remove_backward(self, full_cont: ListInterface, test_values: list[int]):
        assert full_cont.to_list() == test_values
        assert len(full_cont) == len(test_values)

        while len(full_cont) > 0:
            test = full_cont.remove(len(full_cont) - 1)
            comp = test_values.pop(len(test_values) - 1)
            assert test == comp

        assert len(full_cont) == 0
        assert len(full_cont) == len(test_values)
        assert full_cont.to_list() == test_values

    def test_remove_forward(self, full_cont: ListInterface, test_values: list[int]):
        assert full_cont.to_list() == test_values
        assert len(full_cont) == len(test_values)

        while len(full_cont) > 0:
            test = full_cont.remove(0)
            comp = test_values.pop(0)
            assert test == comp

        assert len(full_cont) == 0
        assert len(full_cont) == len(test_values)
        assert full_cont.to_list() == test_values

    def test_remove_random(self, full_cont: ListInterface, test_values: list[int]):
        assert full_cont.to_list() == test_values
        assert len(full_cont) == len(test_values)

        maxindex = len(test_values) - 1
        indexes_to_del = []
        for _ in range(maxindex // 2):
            index = random.randint(0, maxindex)
            indexes_to_del.append(index)

        for index in indexes_to_del:
            test = full_cont.remove(index)
            comp = test_values.pop(index)
            assert test == comp

        assert len(full_cont) == len(test_values)
        assert full_cont.to_list() == test_values

    def test_remove_value_full(self, full_cont: ListInterface, test_values: list[int]):
        for value in test_values:
            full_cont.remove_value(value)
            test_values.pop(test_values.index(value))
            assert full_cont.to_list() == test_values

        assert len(full_cont) == len(test_values)
        assert full_cont.to_list() == test_values

    def test_get_full(self, full_cont: ListInterface, test_values: list[int]):
        for index in range(len(full_cont)):
            test = full_cont.get(index)
            comp = test_values[index]
            assert test == comp

    def test_merge(self, cont: ListInterface, test_values):
        arr1min, arr1max = 0, (len(test_values) - 1) // 2
        arr2min, arr2max = (len(test_values) - 1) // 2, len(test_values) - 1

        arr1 = [random.randint(0, 100) for _ in range(arr1min, arr1max)]
        arr2 = [random.randint(0, 100) for _ in range(arr2min, arr2max)]

        ic1 = copy(cont)
        ic2 = copy(cont)

        for value in arr1:
            ic1.push(value)

        for value in arr2:
            ic2.push(value)

        ic_merged: ListInterface = ic1 + ic2
        arr_merged = arr1 + arr2

        assert ic_merged.to_list() == arr_merged

    def test_replace(self, full_cont: ListInterface, test_values):
        reverse = test_values[::-1]
        for index in range(len(reverse)):
            full_cont.replace(reverse[index], index)

        assert full_cont.to_list() == reverse

    def test_find(self, full_cont: ListInterface, test_values):
        for index in range(len(test_values)):
            value = test_values[index]
            test = full_cont.find(value)
            assert test == index

    def test_reverse(self, full_cont: ListInterface, test_values: list[int]):
        test_values.reverse()
        full_cont.reverse()
        assert full_cont.to_list() == test_values


class TestInterfaceStaticArray(BaseTestInteface):
    @pytest.fixture
    def iclass(self):
        return StaticArray

    @pytest.mark.xfail
    def test_push_overflow(self, cont: ListInterface, test_values):
        return super().test_push_overflow(cont, test_values)

    def test_merge(self, iclass: ListInterface, test_values):
        arr1min, arr1max = 0, (len(test_values) - 2) // 2
        arr2min, arr2max = (len(test_values) - 2) // 2, len(test_values) - 1

        arr1 = [random.randint(0, 100) for _ in range(arr1min, arr1max)]
        arr2 = [random.randint(0, 100) for _ in range(arr2min, arr2max)]

        ic1: ListInterface = iclass(len(test_values))
        ic2: ListInterface = iclass(len(arr2))

        for value in arr1:
            ic1.push(value)

        for value in arr2:
            ic2.push(value)

        ic_merged: ListInterface = ic1 + ic2
        arr_merged = arr1 + arr2

        assert ic_merged.to_list() == arr_merged


class TestInterfaceClassicSinglyLinkedList(BaseTestInteface):
    @pytest.fixture
    def iclass(self):
        return ClassicSinglyLinkedList


class TestInterfaceDynamicArray(BaseTestInteface):
    @pytest.fixture
    def iclass(self):
        return DynamicArray

    def test_push_overflow(self, iclass: ListInterface, test_values):
        cont: ListInterface = iclass(len(test_values) + 3)
        for value in test_values:
            cont.push(value)

        cont.push(100)
        cont.push(200)
        cont.push(300)

        assert cont.to_list() == test_values + [100, 200, 300]

    def test_merge(self, iclass: ListInterface, test_values):
        arr1min, arr1max = 0, (len(test_values) - 2) // 2
        arr2min, arr2max = (len(test_values) - 2) // 2, len(test_values) - 1

        arr1 = [random.randint(0, 100) for _ in range(arr1min, arr1max)]
        arr2 = [random.randint(0, 100) for _ in range(arr2min, arr2max)]

        ic1: ListInterface = iclass(len(test_values))
        ic2: ListInterface = iclass(len(arr2))

        for value in arr1:
            ic1.push(value)

        for value in arr2:
            ic2.push(value)

        ic_merged: ListInterface = ic1 + ic2
        arr_merged = arr1 + arr2

        assert ic_merged.to_list() == arr_merged


class TestInterfaceAdvancedSinglyLinkedList(BaseTestInteface):
    @pytest.fixture
    def iclass(self):
        return AdvancedSinglyLinkedList


class TestInterfaceAdvancedDoublyLinkedList(BaseTestInteface):
    @pytest.fixture
    def iclass(self):
        return AdvancedDoublyLinkedList
