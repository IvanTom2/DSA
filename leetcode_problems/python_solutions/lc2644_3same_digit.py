"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.

Example 1:
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
"""
from time_measure import repeater


class WrongSolution(object):
    def check_target(self, new: str, old: str) -> str:
        if len(new) > len(old) and len(new) >= 3:
            return new

        elif len(new) == len(old) and len(new) >= 3:
            for index in range(len(new)):
                if new[index] > old[index]:
                    return new
            else:
                return old

        else:
            return old

    def run(self, string_number: str) -> str:
        iters = 0
        target = ""

        char = string_number[0]
        start_index = 0

        for current_index in range(1, len(string_number)):
            if string_number[current_index] != char:
                target = self.check_target(
                    string_number[start_index:current_index],
                    target,
                )

                char = string_number[current_index]
                start_index = current_index
                iters += 1

        if iters > 1:
            return target
        else:
            return string_number


class Solution1(object):
    """
    43 ms, 16.5 MB

    Mean time = 0.01113 ms
    Min time  = 0.01049 ms
    """

    def select_biggest(self, targets: list[str]) -> str:
        targets = sorted(targets, reverse=True)
        return targets[0]

    @repeater()
    def run(self, string_number: str) -> str:
        iters = 0
        targets = [""]

        char = ""
        start_index = 0

        for current_index in range(len(string_number)):
            if string_number[current_index] != char:
                if current_index - start_index == 3:
                    targets.append(string_number[start_index:current_index])

                iters = 1
                start_index = current_index
                char = string_number[current_index]

            elif iters == 3:
                targets.append(string_number[start_index:current_index])

                iters = 1
                start_index = current_index
                char = string_number[current_index]

            else:
                iters += 1
        else:
            if iters == 3:
                targets.append(string_number[start_index : current_index + 1])

        targets = self.select_biggest(targets)
        return targets


class Solution2(object):
    """
    33 ms, 16.5 MB

    Mean time = 23 ms
    Min time  = 22.7 ms
    """

    @repeater()
    def run(self, string_number: str) -> str:
        result = ""

        for index in range(2, len(string_number)):
            if (
                string_number[index] == string_number[index - 1]
                and string_number[index] == string_number[index - 2]
            ):
                result = max(result, string_number[index - 2 : index + 1])

        return result


def speed_check_input():
    import random

    inps = list("0123456789")
    lenght = 1000000
    num = "".join([random.choice(inps) for _ in range(lenght)])

    return num


if __name__ == "__main__":
    num = "6777133339"

    sol1 = Solution1()
    sol2 = Solution2()

    spd = speed_check_input()

    print(sol1.run(spd))
    print(sol2.run(spd))
