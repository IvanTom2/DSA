import sys
import pytest
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from stacks import (
    ListStack,
    StaticArrayStack,
    DynamicArrayStack,
    SinglyLinkedListStack,
    DoublyLinkedListStack,
)


class BaseTestStack(object):
    @pytest.fixture
    def stack_cls(self):
        return ListStack

    @pytest.fixture
    def test_values(self):
        return list(range(4))

    @pytest.fixture
    def full_stack(self, stack_cls, test_values):
        stack: ListStack = stack_cls()
        for value in test_values:
            stack.push(value)
        return stack

    def test_push(self, stack_cls, test_values: list[int]):
        stack: ListStack = stack_cls()
        for value in test_values:
            stack.push(value)

        assert stack.to_list() == test_values

    def test_peek(self, full_stack: ListStack, test_values: list[int]):
        test_values.sort()
        while not full_stack.isEmpty():
            peek = full_stack.peek()
            assert peek == test_values.pop()
            full_stack.pop()

        assert len(full_stack) == 0

    def test_pop(self, full_stack: ListStack, test_values: list[int]):
        test_values.sort()
        while not full_stack.isEmpty():
            assert full_stack.pop() == test_values.pop()
        assert len(full_stack) == 0
        assert full_stack.to_list() == []

    def test_empty(self, full_stack: ListStack):
        while not full_stack.isEmpty():
            full_stack.pop()
        assert full_stack.isEmpty()
        assert len(full_stack) == 0
        assert full_stack.to_list() == []


class TestListStack(BaseTestStack):
    @pytest.fixture
    def array_cls(self):
        return ListStack


class TestStaticArrayStack(BaseTestStack):
    @pytest.fixture
    def array_cls(self):
        return StaticArrayStack


class TestDynamicArrayStack(BaseTestStack):
    @pytest.fixture
    def array_cls(self):
        return DynamicArrayStack


class TestSinglyLinkedListStack(BaseTestStack):
    @pytest.fixture
    def array_cls(self):
        return SinglyLinkedListStack


class TestDoublyLinkedListStack(BaseTestStack):
    @pytest.fixture
    def array_cls(self):
        return DoublyLinkedListStack
