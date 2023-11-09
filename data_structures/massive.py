def traversal(
    massive: list[int],
    paces: int,
    forward_traversal: bool = True,
) -> int:
    output = None
    start = 0 if forward_traversal else paces
    paces = paces if forward_traversal else 0
    pointer = paces if forward_traversal else start

    while start <= paces:
        output = massive[pointer]
        start += 1
    return output


def find(massive: list[int], index: int) -> int:
    if index >= 0:
        forward_paces = index
        reverse_paces = len(massive) - index
    else:
        forward_paces = len(massive) + index
        reverse_paces = abs(index)

    forward = True if forward_paces <= reverse_paces else False
    paces = forward_paces if forward else -reverse_paces

    output = traversal(massive, paces, forward)
    return output


massive = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index in map(lambda x: -x, massive):
    found = find(massive, index)
    print(index, found)
