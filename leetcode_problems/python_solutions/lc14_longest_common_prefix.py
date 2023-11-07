"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
from time_measure import repeater


class Solution1(object):
    """
    47 ms, 16.3 MB

    Mean time = 0.01375 ms
    Min time  = 0.01070 ms
    """

    @repeater()
    def run(self, strings: list[str]) -> str:
        word_min_len = min(map(len, strings))

        prefix = ""
        for index in range(word_min_len):
            _set = set(map(lambda x: x[index], strings))
            if len(_set) == 1:
                prefix = prefix + next(_set.__iter__())
            else:
                break

        return prefix


class Solution2(object):
    """
    27 ms, 16.2 MB

    Mean time = 0.00540 ms
    Min time  = 0.00370 ms
    """

    @repeater()
    def run(self, strings: list[str]) -> str:
        prefix = ""

        strings_sort = sorted(strings)
        first, last = strings_sort[0], strings_sort[-1]

        for index in range(min(len(first), len(last))):
            if first[index] == last[index]:
                prefix += first[index]
            else:
                break

        return prefix


if __name__ == "__main__":
    strings = ["flower", "flow", "flight"]

    sol1 = Solution1()
    sol2 = Solution2()

    sol1.run(strings)
    sol2.run(strings)
