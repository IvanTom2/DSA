import sys
import random
import pytest
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from arrays import StaticArray, DynamicArray, SortedArray


class BaseTestArray(object):
    @pytest.fixture
    def array_cls(self):
        return StaticArray

    @pytest.fixture
    def test_values(self):
        return list(range(4))

    @pytest.fixture
    def dop_values(self):
        return list(range(2))

    @pytest.fixture
    def full_array(self, array_cls, test_values):
        array: StaticArray = array_cls(len(test_values))

        for value in test_values:
            array.push(value)

        return array

    def test_push(self, array_cls, test_values):
        array: StaticArray = array_cls(len(test_values))

        for value in test_values:
            array.push(value)

        assert array.to_list() == test_values

    def test_forward_full_insert(self, array_cls, test_values: list[int]):
        array: StaticArray = array_cls(len(test_values))

        for value in test_values:
            array.insert(value, 0)

        test_values.sort(reverse=True)
        assert array.to_list() == test_values

    def test_consecutive_full_insert(self, array_cls, test_values):
        array: StaticArray = array_cls(len(test_values))

        for index in range(len(test_values)):
            array.insert(test_values[index], index)

        assert array.to_list() == test_values

    def test_push_insert(self, array_cls, test_values):
        array: StaticArray = array_cls(len(test_values))

        for index in range(len(test_values)):
            mode = random.random()
            if mode >= 0.5:
                array.push(test_values[index])
            else:
                array.insert(test_values[index], index)

        assert array.to_list() == test_values

    def test_forward_insert(
        self,
        array_cls,
        test_values: list[int],
        dop_values: list[int],
    ):
        array: StaticArray = array_cls(len(test_values) + len(dop_values))

        for value in test_values:
            array.push(value)

        for value in dop_values:
            array.insert(value, 0)

        dop_values.sort(reverse=True)
        assert array.to_list() == dop_values + test_values

    def test_back_insert(
        self,
        array_cls,
        test_values: list[int],
        dop_values: list[int],
    ):
        array: StaticArray = array_cls(len(test_values) + len(dop_values))

        for value in test_values:
            array.push(value)

        index = len(test_values)
        for value in dop_values:
            array.insert(value, index)
            index += 1

        assert array.to_list() == test_values + dop_values

    def test_get(
        self,
        full_array: StaticArray,
        test_values: list[int],
    ):
        for index in range(len(test_values)):
            assert test_values[index] == full_array.get(index)

    def test_pop(self, full_array: StaticArray, test_values: list[int]):
        for index in range(1, len(test_values) + 1):
            assert test_values[-index] == full_array.pop()

    def test_forward_remove(self, full_array: StaticArray, test_values: list[int]):
        for index in range(len(test_values)):
            assert test_values[index] == full_array.remove(0)

    def test_backward_remove(self, full_array: StaticArray, test_values: list[int]):
        for index in range(1, len(test_values) + 1):
            assert test_values[-index] == full_array.remove(len(full_array) - 1)

    def test_middle_remove(self, full_array: StaticArray):
        lst = full_array.to_list()

        target = full_array.get(1)
        val = full_array.remove(1)
        assert val == target
        lst.pop(1)
        assert full_array.to_list() == lst

        target = full_array.get(1)
        val = full_array.remove(1)
        assert val == target
        lst.pop(1)
        assert full_array.to_list() == lst

    @pytest.mark.xfail
    def test_limit_push_fail(self, full_array: StaticArray):
        full_array.push(0)

    @pytest.mark.xfail
    def test_limit_insert_fail(self, full_array: StaticArray):
        full_array.insert(0, 0)

    @pytest.mark.xfail
    def test_overflow_index_insert_fail(self, full_array: StaticArray):
        full_array.insert(0, len(full_array) + 1)

    @pytest.mark.xfail
    def test_inappropriate_index_insert_fail(self, array_cls, test_values):
        array: StaticArray = array_cls(len(test_values))
        array.insert(0, 2)

    @pytest.mark.xfail
    def test_inapppropriate_index_get_fail(self, full_array: StaticArray):
        full_array.get(len(full_array) + 1)

    @pytest.mark.xfail
    def test_inapppropriate_pop_fail(self, full_array: StaticArray):
        for _ in range(len(full_array)):
            full_array.pop()
        full_array.pop()

    @pytest.mark.xfail
    def test_inapppropriate_remove_fail(self, full_array: StaticArray):
        for _ in range(len(full_array)):
            full_array.remove(0)
        full_array.remove(0)


class TestStaticArray(BaseTestArray):
    @pytest.fixture
    def array_cls(self):
        return StaticArray


class TestDynamicArray(BaseTestArray):
    @pytest.fixture
    def array_cls(self):
        return DynamicArray

    def test_limit_push_fail(self, full_array: DynamicArray):
        # should pass in dynamic array
        full_array.push(0)

    def test_limit_insert_fail(self, full_array: DynamicArray):
        # should pass in dynamic array
        full_array.insert(0, 0)
