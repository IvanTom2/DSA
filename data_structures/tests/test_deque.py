import sys
import pytest
import random
from pathlib import Path


from deques import ListDeque, DequeInterface, DynamicArrayDeque, SLLDeque, DLLDeque


class BaseTestDeque(object):
    @pytest.fixture
    def deque_cls(self):
        return DequeInterface

    @pytest.fixture
    def test_values(self):
        return list(range(4))

    @pytest.fixture
    def full_deque(self, deque_cls, test_values):
        deque: DequeInterface = deque_cls()
        for value in test_values:
            deque.push_back(value)

        return deque

    def test_push_front(self, deque_cls, test_values: list[int]):
        deque: DequeInterface = deque_cls()
        for value in test_values:
            deque.push_front(value)

        test_values.sort(reverse=True)
        assert deque.to_list() == test_values

    def test_push_back(self, deque_cls, test_values: list[int]):
        deque: DequeInterface = deque_cls()
        for value in test_values:
            deque.push_back(value)

        assert deque.to_list() == test_values

    def test_pop_front(
        self,
        full_deque: DequeInterface,
        test_values: list[int],
    ):
        while not full_deque.isEmpty():
            value = full_deque.pop_front()
            test_value = test_values.pop(0)

            assert value == test_value

        assert full_deque.to_list() == test_values
        assert full_deque.isEmpty()
        assert len(full_deque) == 0

    def test_pop_back(
        self,
        full_deque: DequeInterface,
        test_values: list[int],
    ):
        test_values.sort(reverse=True)
        while not full_deque.isEmpty():
            value = full_deque.pop_back()
            test_value = test_values.pop(0)

            assert value == test_value

        assert full_deque.to_list() == test_values
        assert full_deque.isEmpty()
        assert len(full_deque) == 0

    def test_pop_front_back(
        self,
        full_deque: DequeInterface,
        test_values: list[int],
    ):
        while not full_deque.isEmpty():
            if random.random() >= 0.5:
                value = full_deque.pop_front()
                test_value = test_values.pop(0)
            else:
                value = full_deque.pop_back()
                test_value = test_values.pop()

            assert value == test_value

        assert full_deque.to_list() == test_values
        assert full_deque.isEmpty()
        assert len(full_deque) == 0

    def test_push_front_back(
        self,
        deque_cls,
        test_values: list[int],
    ):
        array = []
        deque: DequeInterface = deque_cls()
        for value in test_values:
            if random.random() >= 0.5:
                deque.push_back(value)
                array.append(value)
            else:
                deque.push_front(value)
                array.insert(0, value)

        assert deque.to_list() == array


class TestListDeque(BaseTestDeque):
    @pytest.fixture
    def deque_cls(self):
        return ListDeque


class TestDynamicArrayDeque(BaseTestDeque):
    @pytest.fixture
    def deque_cls(self):
        return DynamicArrayDeque


class TestSLLDeque(BaseTestDeque):
    @pytest.fixture
    def deque_cls(self):
        return SLLDeque


class TestDLLDeque(BaseTestDeque):
    @pytest.fixture
    def deque_cls(self):
        return DLLDeque
