import sys
from time_measure import repeater

sys.setrecursionlimit(2500)


class InsertionSort(object):
    """
    Mean time = 173.80724 ms
    Min time  = 167.60172 ms
    """

    # @repeater()
    def sort(self, numbers: list[int]):
        for key_index in range(1, len(numbers)):
            key = numbers[key_index]

            insert_index = key_index - 1
            while numbers[insert_index] > key and insert_index >= 0:
                numbers[insert_index + 1] = numbers[insert_index]
                insert_index -= 1

            numbers[insert_index + 1] = key


class InsertionSortRecursive(object):
    """
    Mean time = 737.13980 ms
    Min time  = 726.76494 ms
    """

    def insertion_rec(
        self,
        numbers: list[int],
        key: int,
        insert_index: int,
    ):
        if insert_index >= 0 and numbers[insert_index] > key:
            numbers[insert_index + 1] = numbers[insert_index]
            self.insertion_rec(numbers, key, insert_index - 1)
        else:
            numbers[insert_index + 1] = key

    def insertion_sort_rec(
        self,
        numbers: list[int],
        key_index,
    ):
        self.insertion_rec(numbers, numbers[key_index], key_index - 1)
        key_index += 1

        if key_index < len(numbers):
            self.insertion_sort_rec(numbers, key_index)

    # @repeater()
    def sort(self, numbers: list[int]):
        self.insertion_sort_rec(numbers, 1)


if __name__ == "__main__":
    numbers = list(range(1000)[::-1])

    # sorter = InsertionSort()
    sorter = InsertionSortRecursive()

    sorter.sort(numbers)
    assert list(range(1000)) == numbers
