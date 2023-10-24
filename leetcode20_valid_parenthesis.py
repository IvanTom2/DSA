"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true
"""


class WrongSolution(object):
    """"""

    def slicer(
        self,
        string: str,
        step: int,
        start: int = 0,
    ) -> str:
        iters = len(string) // step + (len(string) % step > 0)

        for _ in range(iters):
            yield string[start : start + step]
            start += step

    def run(self, string: str) -> bool:
        patterns = set(["()", "[]", "{}"])

        for slice in self.slicer(string, 2):
            if slice not in patterns:
                return False

        return True


class Solution(object):
    def run(self, string: str) -> bool:
        pass


if __name__ == "__main__":
    string = "{[]}"

    sol = Solution()
    print(sol.run(string))
