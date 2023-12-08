from copy import deepcopy


class Sorter(object):
    def sort(self):
        pass


class MergeSortRecursive(object):
    def merge(
        self,
        numbers: list[int],
        begin: int,
        middle: int,
        end: int,
    ):
        n1 = middle - begin + 1
        n2 = end - middle

        newList1 = []
        newList2 = []

        for index in range(begin, middle + 1):
            newList1.append(numbers[index])

        for index in range(middle + 1, end + 1):
            newList2.append(numbers[index])

        i, j, k = 0, 0, begin
        while i < n1 and j < n2:
            if newList1[i] <= newList2[j]:
                numbers[k] = newList1[i]
                i += 1
            else:
                numbers[k] = newList2[j]
                j += 1

            k += 1

        while i < n1:
            numbers[k] = newList1[i]
            i += 1
            k += 1

        while j < n2:
            numbers[k] = newList2[j]
            j += 1
            k += 1

    def merge_sort_rec_func(
        self,
        numbers: list[int],
        begin: int,
        end: int,
    ):
        if begin < end:
            middle = begin + (end - begin) // 2
            self.merge_sort_rec_func(numbers, begin, middle)
            self.merge_sort_rec_func(numbers, middle + 1, end)
            self.merge(numbers, begin, middle, end)

    def sort(self, numbers: list[int]):
        begin = 0
        end = len(numbers) - 1
        self.merge_sort_rec_func(numbers, begin, end)


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
    # fast_test(MergeSortRecursive)

    # numbers = list(range(1000)[::-1])
    numbers = [4, 3, 2, 1]

    sorter = MergeSortRecursive()
    sorter.sort(numbers)

    print(numbers)
