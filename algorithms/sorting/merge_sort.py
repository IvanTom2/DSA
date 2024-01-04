import math
from copy import deepcopy


class Sorter(object):
    def sort(self):
        pass


class MergeSortRecursive(object):
    def merge(
        self,
        array: list[int],
        low: int,
        mid: int,
        high: int,
    ) -> None:
        n1 = mid - low + 1
        n2 = high - mid

        left = [array[low + i] for i in range(n1)]
        right = [array[mid + 1 + j] for j in range(n2)]

        i, j, k = 0, 0, low
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < n1:
            array[k] = left[i]
            i += 1
            k += 1

        while j < n2:
            array[k] = right[j]
            j += 1
            k += 1

    def msrf(
        self,
        array: list[int],
        low: int,
        high: int,
    ) -> None:
        if low < high:
            mid = low + (high - low) // 2
            self.msrf(array, low, mid)
            self.msrf(array, mid + 1, high)
            self.merge(array, low, mid, high)

    def sort(self, array: list[int]) -> None:
        low, high = 0, len(array) - 1
        self.msrf(array, low, high)


class MergeSort(object):
    def merge(
        self,
        array: list[int],
        low: int,
        mid: int,
        high: int,
    ) -> None:
        if low >= high:
            return

        i = low
        j = mid + 1
        k = 0
        size = high - low + 1

        arr = [0] * size
        while i <= mid and j <= high:
            if array[i] < array[j]:
                arr[k] = array[i]
                i += 1
            else:
                arr[k] = array[j]
                j += 1

            k += 1

        while i <= mid:
            arr[k] = array[i]
            i += 1
            k += 1

        while j <= high:
            arr[k] = array[j]
            j += 1
            k += 1

        for index in range(size):
            array[low + index] = arr[index]

    def msrf(
        self,
        array: list[int],
        low: int,
        high: int,
    ) -> None:
        if low < high:
            mid = low + (high - low) // 2
            self.msrf(array, low, mid)
            self.msrf(array, mid + 1, high)
            self.merge(array, low, mid, high)

    def sort(self, array: list[int]) -> None:
        self.msrf(array, 0, len(array) - 1)


class MergeSortInplace(object):
    def merge(
        self,
        array: list[int],
        low: int,
        mid: int,
        high: int,
    ) -> None:
        if low >= high:
            return

        i, j = low, mid + 1
        while i <= mid and j <= high:
            if array[i] <= array[j]:
                i += 1
            else:
                value = array[j]
                for k in range(j, i, -1):
                    array[k] = array[k - 1]
                array[i] = value
                j += 1
                i += 1
                mid += 1

    def msrf(
        self,
        array: list[int],
        low: int,
        high: int,
    ) -> None:
        if low < high:
            mid = low + (high - low) // 2
            self.msrf(array, low, mid)
            self.msrf(array, mid + 1, high)
            self.merge(array, low, mid, high)

    def sort(self, array: list[int]) -> None:
        self.msrf(array, 0, len(array) - 1)


class MergeSortY(object):
    def sort(self, array: list[int]) -> list[int]:
        if len(array) == 1:
            return array

        left = self.sort(array[0 : len(array) // 2])
        right = self.sort(array[len(array) // 2 : len(array)])

        result = [None] * len(array)
        l, r, k = 0, 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result[k] = left[l]
                l += 1
            else:
                result[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            result[k] = left[l]
            l += 1
            k += 1

        while k < len(right):
            result[k] = right[r]
            r += 1
            k += 1

        return result


def fast_test(sorter: Sorter):
    sorter: Sorter = sorter()

    l = []
    lc = deepcopy(l)
    sorter.sort(l)
    assert l == list(sorted(lc))

    l = [4, 3, 2, 1]
    lc = deepcopy(l)
    sorter.sort(l)
    assert l == list(sorted(lc))

    l = [42]
    lc = deepcopy(l)
    sorter.sort(l)
    assert l == list(sorted(lc))

    l = [4, 3]
    lc = deepcopy(l)
    sorter.sort(l)
    assert l == list(sorted(lc))

    l = [1, 2, 3, 4]
    lc = deepcopy(l)
    sorter.sort(l)
    assert l == list(sorted(lc))

    l = [-1, -2, 4, 3, -6]
    lc = deepcopy(l)
    sorter.sort(l)
    assert l == list(sorted(lc))

    l = list(range(100))
    lc = deepcopy(l)
    sorter.sort(l)
    assert l == list(sorted(lc))


if __name__ == "__main__":
    # fast_test(MergeSortInplace)

    numbers = list(range(1000)[::-1])
    # numbers = [4, 3, 2, 1]
    # numbers = [3, 2, 4, 7, 6, 9]
    # numbers = [-1, -2, 4, 3, -6]

    sorter = MergeSortY()
    sorter.sort(numbers)

    print(numbers)
