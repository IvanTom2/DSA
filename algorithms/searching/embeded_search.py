def find_index_recfunc(
    array: list[int],
    target: int,
    container: list[int],
) -> list[int]:
    for index, element in enumerate(array):
        if isinstance(element, list):
            nested = container + [index]
            result = find_index_recfunc(element, target, nested)
            if result is not None:
                return result

        elif element == target:
            return container + [index]

    return None


def find_index_recursively(
    array: list[int],
    target: int,
) -> list[int]:
    return find_index_recfunc(array, target, [])


def find_index(array: list[int], target: int) -> list[int]:
    stack = [(array, [])]

    while stack:
        cur_array, current_index = stack.pop()

        for index, element in enumerate(cur_array):
            if isinstance(element, list):
                stack.append((element, current_index + [index]))
            elif element == target:
                return current_index + [index]

    return None


def print_num(array: list[int], indexer: list[int]):
    for index in indexer:
        array = array[index]
    print("index is:", indexer, "number is:", array)


def example() -> tuple[list[int], int]:
    TARGET = 111

    array = [
        [
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
        ],
        [
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
        ],
        [
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, [1, [1, [1, 1, TARGET]]], 6], [7, 8, 9], [10, 11, 12]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            ],
        ],
    ]

    return array, TARGET


if __name__ == "__main__":
    array, target = example()

    indexer1 = find_index_recursively(array, target)
    indexer2 = find_index(array, target)

    print(indexer1)
    print(indexer2)

    print_num(array, indexer1)
    print_num(array, indexer2)
