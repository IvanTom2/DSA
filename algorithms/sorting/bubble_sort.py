class BubbleSort(object):
    def sort(self, array: list[int]) -> None:
        for p1 in range(len(array) - 1):
            for p2 in range(len(array) - 1, p1, -1):
                if array[p1] > array[p2]:
                    array[p1], array[p2] = array[p2], array[p1]


if __name__ == "__main__":
    array = [4, 3, 2, 5, 1, 4, 0]

    sorter = BubbleSort()
    sorter.sort(array)

    print(array)
