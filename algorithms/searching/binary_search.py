def binary_search(array, item):
    low, high = 0, len(array)

    while low <= high:
        mid = (low + high) // 2
        search = array[mid]

        if search == item:
            return mid

        if search > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(binary_search(a, 5))
