def linear_search(array: list[int], element: int) -> int:
    for index in range(len(array)):
        if array[index] == element:
            return index
    return None


if __name__ == "__main__":
    array = [3, 1, 4, 51, 3, 16, 4, 3, 2, 6, 17, 54, 4]

    print(linear_search(array, 16))
