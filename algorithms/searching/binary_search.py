def binary_search(array: list[int], value: int) -> int:
    low, high = 0, len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == value:
            return mid

        if array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    return None


def insert_binary_search(array: list[int], value: int) -> int:
    low, high = 0, len(array)

    while low < high:
        mid = low + (high - low) // 2

        if array[mid] == value:
            return mid

        if array[mid] > value:
            high = mid
        else:
            low = mid + 1

    return low


if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5]

    # print(binary_search(array, 0))
    pos = insert_binary_search(array, 7)
    print(pos)
