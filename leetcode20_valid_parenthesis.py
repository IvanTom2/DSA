"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true
"""
from line_profiler import profile as cpu_profile


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
    """27 ms, 16.3 MB"""

    chars = {"(": ")", "{": "}", "[": "]"}

    def run(self, string: str) -> bool:
        if len(string) % 2 == 0:
            stack = []
            for char in string:
                if char in self.chars:
                    stack.append(char)
                elif not stack or self.chars[stack.pop()] != char:
                    return False

            return len(stack) == 0

        else:
            return False


class Solution2(object):
    def run(self, s):
        if len(s) % 2 != 0:
            return False
        opening = set("([{")
        matches = set([("(", ")"), ("[", "]"), ("{", "}")])
        stack = []

        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if (last_open, paren) not in matches:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    string = "{[]}"
    string = "{[]}[]()"

    sol = Solution()
    print(sol.run(string))
