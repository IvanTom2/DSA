import sys
from pathlib import Path
from typing import Union

sys.path.append(str(Path(__file__).parent.parent))
from arrays import Array, DynamicArray, SortedArray
from memory_model import EmptyMemoryCell
import pytest


class TestArray:
    @pytest.fixture
    def test_values(self):
        return list(range(4))

    @pytest.fixture
    def full_array(self, test_values):
        values = test_values
        array = Array(4)

        for value in values:
            array.push(value)

        return array

    def test_push(self):
        values = range(4)
        array = Array(4)

        for value in values:
            array.push(value)

        assert array.to_list() == list(values)

    def test_forward_full_insert(self):
        values = range(4)
        array = Array(4)

        for value in values:
            array.insert(value, 0)

        assert array.to_list() == [3, 2, 1, 0]

    def test_consecutive_full_insert(self):
        values = list(range(4))
        array = Array(4)

        for index in range(len(values)):
            array.insert(values[index], index)

        assert array.to_list() == values

    def test_middle_insert(self):
        array = Array(4)
        array.push(0)
        array.push(0)
        array.push(0)
        array.insert(1, 2)

        assert array.to_list() == [0, 0, 1, 0]

    def test_forward_insert(self):
        array = Array(4)
        array.push(0)
        array.push(0)
        array.push(0)
        array.insert(1, 0)

        assert array.to_list() == [1, 0, 0, 0]

    def test_back_insert(self):
        array = Array(4)
        array.push(0)
        array.push(0)
        array.push(0)
        array.insert(1, 3)

        assert array.to_list() == [0, 0, 0, 1]

    def test_get(self, full_array: Array, test_values: list[int]):
        for index in range(len(test_values)):
            assert test_values[index] == full_array.get(index)

    def test_pop(self, full_array: Array, test_values: list[int]):
        for index in range(1, len(test_values) + 1):
            assert test_values[-index] == full_array.pop()

    def test_forward_remove(self, full_array: Array, test_values: list[int]):
        for index in range(len(test_values)):
            assert test_values[index] == full_array.remove(0)

    def test_backward_remove(self, full_array: Array, test_values: list[int]):
        for index in range(1, len(test_values) + 1):
            assert test_values[-index] == full_array.remove(len(full_array) - 1)

    def test_middle_remove(self, full_array: Array):
        val = full_array.remove(1)
        assert val == 1
        assert full_array.to_list() == [0, 2, 3]

        val = full_array.remove(1)
        assert val == 2
        assert full_array.to_list() == [0, 3]

    @pytest.mark.xfail
    def test_limit_push(self, full_array: Array):
        full_array.push(0)

    @pytest.mark.xfail
    def test_limit_insert(self, full_array: Array):
        full_array.insert(0, 0)

    @pytest.mark.xfail
    def test_overflow_index_insert(self):
        array = Array(4)
        array.insert(0, 4)

    @pytest.mark.xfail
    def test_inappropriate_index_insert(self):
        array = Array(4)
        array.insert(0, 2)

    @pytest.mark.xfail
    def test_inapppropriate_index_get(self, full_array: Array):
        full_array.get(5)

    @pytest.mark.xfail
    def test_inapppropriate_pop(self, full_array: Array):
        for _ in range(5):
            full_array.pop()

    @pytest.mark.xfail
    def test_inapppropriate_remove(self, full_array: Array):
        for _ in range(5):
            full_array.remove(0)
