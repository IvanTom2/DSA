import base
from memory_model import Memory, NotAllowedMemoryCell, MemoryCell, EmptyMemoryCell
import pytest


class TestMemory(object):
    @pytest.fixture
    def small(self):
        size, large = 4, 4
        return size, large

    @pytest.fixture
    def mid(self):
        size, large = 16, 16
        return size, large

    @pytest.fixture
    def large(self):
        size, large = 100, 25
        return size, large

    @pytest.fixture
    def small_memory(self, small):
        size, large = small
        return Memory(size, large)

    @pytest.fixture
    def mid_memory(self, mid):
        size, large = mid
        return Memory(size, large)

    @pytest.fixture
    def large_memory(self, large):
        size, large = large
        return Memory(size, large)

    @pytest.fixture
    def allocated_small_memory(self, small_memory: Memory):
        small_memory.allocate()
        return small_memory

    def test_memory_size(
        self,
        small_memory: Memory,
        small,
        mid_memory: Memory,
        mid,
        large_memory: Memory,
        large,
    ):
        assert small_memory._size == small[0]
        assert mid_memory._size == mid[0]
        assert large_memory._size == large[0]

    def test_memory_large(
        self,
        small_memory: Memory,
        small,
        mid_memory: Memory,
        mid,
        large_memory: Memory,
        large,
    ):
        assert len(small_memory.storage) == small[0] * small[1]
        assert len(mid_memory.storage) == mid[0] * mid[1]
        assert len(large_memory.storage) == large[0] * large[1]

    def test_access(self, allocated_small_memory: Memory):
        middle = len(allocated_small_memory.storage) // 2

        assert isinstance(allocated_small_memory.access(middle), MemoryCell)
        assert isinstance(allocated_small_memory.access(0), NotAllowedMemoryCell)

    @pytest.mark.xfail(strict=True)
    def test_fail_access(self, allocated_small_memory: Memory):
        limit = len(allocated_small_memory.storage)

        overlimit = allocated_small_memory.access(limit + 10)

    def test_memory_cell(self):
        cell = MemoryCell()
        assert isinstance(cell.get(), EmptyMemoryCell)

        cell.assign(4)
        assert cell.get() == 4

        cell.assign(10)
        assert cell.get() == 10

    def test_memory_allocation(self):
        mem = Memory(4, 4)
        cells = set(mem.storage)
        cells == set([NotAllowedMemoryCell()])

        mem.allocate()
        cells = set(mem.storage)
        cells = set([NotAllowedMemoryCell(), MemoryCell()])
