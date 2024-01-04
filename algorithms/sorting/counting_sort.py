import random


class CountingSort(object):
    def sort(
        self,
        array: list[int],
        vrange: range,
    ):
        vmin = vrange.start
        uvalues = [0 for _ in vrange]

        for value in array:
            uvalues[value] += 1

        index = 0
        pointer = 0
        while pointer < len(uvalues):
            if uvalues[pointer] > 0:
                array[index] = vmin + pointer
                uvalues[pointer] -= 1
                index += 1
            else:
                pointer += 1


if __name__ == "__main__":
    array = list(range(10, -1, -1))

    sorter = CountingSort()
    sorter.sort(array, range(0, 11))

    print(array)
