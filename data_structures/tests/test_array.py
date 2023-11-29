import sys
from pathlib import Path
from typing import Union

sys.path.append(str(Path(__file__).parent.parent))
from arrays import Array, DynamicArray


def test_push() -> None:
    values = [0, 1, 2, 3, 4]

    array = Array(5)
    lst = list()

    for value in values:
        array.push(value)
        lst.append(value)

        assert array.to_list() == lst


def test_fill_from() -> None:
    lst = [1, 2, 3, 4, 5]

    array = Array(5)
    array.fill_from(lst)

    assert array.to_list() == lst


def test_pop() -> None:
    values = [1, 2, 3, 4, 5]

    lst = list(values)
    array = Array(5)
    array.fill_from(values)

    assert array.to_list() == lst

    for value in lst[::-1]:
        poped = array.pop()
        assert poped == value

    assert len(array) == 0


def test_remove() -> None:
    values = [1, 2, 3, 4, 5]

    lst = list(values)
    array = Array(5)
    array.fill_from(values)

    assert array.to_list() == lst

    indexes = [4, 2, 0, 1, 0]
    for index in indexes:
        arr_val = array.remove(index)
        list_val = lst.pop(index)

        assert arr_val == list_val

    assert len(array) == 0


def test_insert() -> None:
    lst = [1, 2, 3, 4, 5]

    array = Array(5)
    array.insert(2, 0)
    array.insert(3, 1)
    array.insert(1, 0)
    array.insert(5, 3)
    array.insert(4, 3)

    assert lst == array.to_list()


def test_Array():
    test_push()


if __name__ == "__main__":
    test_Array()
