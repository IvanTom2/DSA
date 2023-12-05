import base
from memory_model import Memory, NotAllowedMemoryCell, MemoryCell
import pytest


@pytest.fixture
def small():
    size, large = 4, 4
    return size, large


@pytest.fixture
def mid():
    size, large = 16, 16
    return size, large


@pytest.fixture
def large():
    size, large = 100, 25
    return size, large


@pytest.fixture
def small_memory(small):
    size, large = small
    return Memory(size, large)


@pytest.fixture
def mid_memory(mid):
    size, large = mid
    return Memory(size, large)


@pytest.fixture
def large_memory(large):
    size, large = large
    return Memory(size, large)


@pytest.fixture
def allocated_small_memory(small_memory):
    small_memory.allocate()
    return small_memory


def test_memory_size(small_memory, small, mid_memory, mid, large_memory, large):
    assert small_memory._size == small[0]
    assert mid_memory._size == mid[0]
    assert large_memory._size == large[0]


def test_memory_large(small_memory, small, mid_memory, mid, large_memory, large):
    assert len(small_memory.storage) == small[0] * small[1]
    assert len(mid_memory.storage) == mid[0] * mid[1]
    assert len(large_memory.storage) == large[0] * large[1]


def test_access(allocated_small_memory):
    middle = len(allocated_small_memory.storage) // 2

    assert isinstance(allocated_small_memory.access(middle), MemoryCell)
    assert isinstance(allocated_small_memory.access(0), NotAllowedMemoryCell)


@pytest.mark.xfail(strict=True)
def test_fail_access(allocated_small_memory):
    limit = len(allocated_small_memory.storage)

    overlimit = allocated_small_memory.access(limit + 10)


def test_memory_cell():
    cell = MemoryCell(4)
    assert cell.get() == 4

    cell.assign(10)
    assert cell.get() == 10


def test_memory_allocation():
    mem = Memory(4, 4)
    cells = set(mem.storage)
    cells == set([NotAllowedMemoryCell()])

    mem.allocate()
    cells = set(mem.storage)
    cells = set([NotAllowedMemoryCell(), MemoryCell("E")])
