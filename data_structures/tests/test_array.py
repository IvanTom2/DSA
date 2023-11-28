import sys
from pathlib import Path
from typing import Union

sys.path.append(str(Path(__file__).parent.parent))
from arrays import Array, DynamicArray


def compare_to_list(
    array: Union[Array, DynamicArray],
    massive: list,
    reverse_massive: bool = False,
):
    if reverse_massive:
        if isinstance(massive, list):
            massive.reverse()
        else:
            massive = list(massive)
            massive.reverse()

    mList = map(lambda x: x.value, array)
    result = map(lambda x: x[0] - x[1], zip(mList, massive))
    assert set(result) == set([0])


def test_push(arrayClass: Union[Array, DynamicArray]) -> None:
    vals = [0, 1, 2, 3, 4]
    array: Array = arrayClass(len(vals))

    for val in vals:
        array.push(val)

    print(array)

    # compare_to_list(array, vals)


def arrayTests(arrayClass: Union[Array, DynamicArray]) -> None:
    test_push(arrayClass)


def test_Array():
    arrayTests(Array)


if __name__ == "__main__":
    test_Array()
