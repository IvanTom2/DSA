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


def bsrf(
    array: list[int],
    value: int,
    low: int,
    high: int,
) -> int:
    """binary search recursive function"""
    mid = low + (high - low) // 2
    if value == array[mid]:
        return mid
    if value < array[mid]:
        srch = bsrf(array, value, low, mid)
    else:
        srch = bsrf(array, value, mid + 1, high)
    output = srch if srch == value else None
    return output


def binary_search_resursive(array: list[int], value: int) -> int:
    return bsrf(array, value, 0, len(array) - 1)


if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5]

    print(binary_search_resursive(array, 4))
