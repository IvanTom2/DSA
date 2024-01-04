import random


class QuickSortRandom(object):
    def partition(
        self,
        array: list[int],
        pivot: int,
    ) -> tuple[list[int], list[int], list[int]]:
        less = [i for i in array if i < pivot]
        center = [i for i in array if i == pivot]
        greater = [i for i in array if i > pivot]
        return less, center, greater

    def sort(self, array: list[int]) -> list[int]:
        if len(array) < 2:
            return array
        else:
            pivot = random.choice(array)
            less, center, greater = self.partition(array, pivot)
            return self.sort(less) + center + self.sort(greater)


if __name__ == "__main__":
    array = [4, 3, 2, 1]

    sorter = QuickSortRandom()
    sorter.sort(array)

    print(array)
