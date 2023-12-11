"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
"""
from time_measure import repeater


class Solution1(object):
    """
    30 ms, 16.5 MB

    Mean time = 0.81694 ms
    Min time  = 0.79265 ms
    """

    @repeater()
    def run(self, string: str) -> str:
        string = list(map(lambda x: x.strip(), string.split()))
        return " ".join(string[::-1])


class Solution2(object):
    """
    39 ms, 16.5 MB

    Mean time = 1.89177 ms
    Min time  = 1.86140 ms
    """

    @repeater()
    def run(self, string: str) -> str:
        newStr = []
        stack = []

        word = ""
        for char in string:
            if char != " ":
                word += char
            else:
                if word:
                    stack.append(word)
                    word = ""
        else:
            if word:
                stack.append(word)

        while stack:
            word = stack.pop()
            newStr.append(word)

        return " ".join(newStr)


if __name__ == "__main__":
    string = " ".join(["abcabc" for _ in range(1000)])

    sol1 = Solution1()
    sol2 = Solution2()

    sol1.run(string)
    sol2.run(string)
