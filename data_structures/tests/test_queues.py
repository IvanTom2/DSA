import sys
import pytest
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from queues import (
    ListQueue,
    DynamicArrayQueue,
    SLLQueue,
    DLLQueue,
    ListLazyQueue,
    DynamicArrayLazyQueue,
    SLLLazyQueue,
    DLLLazyQueue,
)


def compare(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    else:
        index = 0
        while index < len(arr1):
            equal = arr1[index] == arr2[index]
            if not equal:
                return False
            index += 1
        return True


class BaseTest(object):
    @pytest.fixture
    def queue_cls(self):
        return ListQueue

    @pytest.fixture
    def test_values(self):
        return list(range(4))

    @pytest.fixture
    def full_queue(
        self,
        queue_cls,
        test_values: list[int],
    ) -> ListQueue:
        queue: ListQueue = queue_cls()
        for value in test_values:
            queue.enqueue(value)

    def test_enqueue(self, queue_cls, test_values: list[int]):
        queue: ListQueue = queue_cls()
        for value in test_values:
            queue.enqueue(value)

        assert compare(queue.to_list(), test_values)

    def test_dequeue(self, queue_cls, test_values: list[int]):
        queue: ListQueue = queue_cls()
        while not queue.isEmpty():
            queue_value = queue.dequeue()
            test_value = test_values.pop(0)
            assert queue_value == test_value

        assert queue.isEmpty()

    def test_peek(self, queue_cls, test_values: list[int]):
        queue: ListQueue = queue_cls()
        index = 0
        for value in test_values:
            queue.enqueue(value)
            peeked = queue.peek()
            assert peeked == test_values[index]

        assert compare(queue.to_list(), test_values)

    def test_isEmpty(self, queue_cls, test_values: list[int]):
        queue: ListQueue = queue_cls()
        assert queue.isEmpty()

        for value in test_values:
            queue.enqueue(value)
            assert not queue.isEmpty()

        while not queue.isEmpty():
            queue.dequeue()

        assert queue.isEmpty()


class TestListQueue(BaseTest):
    @pytest.fixture
    def queue_cls(self):
        return ListQueue


class TestDynamicArrayQueue(BaseTest):
    @pytest.fixture
    def queue_cls(self):
        return DynamicArrayQueue


class TestSLLQueue(BaseTest):
    @pytest.fixture
    def queue_cls(self):
        return SLLQueue


class TestDLLQueue(BaseTest):
    @pytest.fixture
    def queue_cls(self):
        return DLLQueue


class TestListLazyQueue(BaseTest):
    @pytest.fixture
    def queue_cls(self):
        return ListLazyQueue


class TestDynamicArrayLazyQueue(BaseTest):
    @pytest.fixture
    def queue_cls(self):
        return DynamicArrayLazyQueue


class TestSLLLazyQueue(BaseTest):
    @pytest.fixture
    def queue_cls(self):
        return SLLLazyQueue


class TestDLLLazyQueue(BaseTest):
    @pytest.fixture
    def queue_cls(self):
        return DLLLazyQueue
