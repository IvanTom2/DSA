"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
from time_measure import repeater


class Solution1(object):
    """
    47 ms, 22.4 MB

    Mean time = 0.01641 ms
    Min time  = 0.01430 ms
    """

    symb = set("abcdefghijklmnopqrstuvwxyz0123456789")

    @repeater()
    def run(self, string: str) -> bool:
        string = [s.lower() for s in string if s.lower() in self.symb]
        return string == string[::-1]


class Solution2(object):
    """
    56 ms, 22.2 MB

    Mean time = 0.02306 ms
    Min time  = 0.01950 ms
    """

    symb = set("abcdefghijklmnopqrstuvwxyz0123456789")

    @repeater()
    def run(self, string: str) -> bool:
        string = [s.lower() for s in string if s.lower() in self.symb]
        if len(string) == 1:
            return True

        back = len(string) - 1
        front = 0

        while back > front:
            if string[front] != string[back]:
                return False

            front += 1
            back -= 1

        return True


class Solution3(object):
    """
    46 ms, 16.9 MB

    Mean time = 0.02223 ms
    Min time  = 0.01710 ms
    """

    @repeater()
    def run(self, string: str) -> bool:
        l, r = 0, len(string) - 1
        while l < r:
            if not string[l].isalnum():
                l += 1
            elif not string[r].isalnum():
                r -= 1
            else:
                if string[l].lower() != string[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True


class Solution4(object):
    """
    33 ms, 22.5 MB

    Mean time = 0.01375 ms
    Min time  = 0.01110 ms
    """

    @repeater()
    def run(self, string: str) -> bool:
        string = [i.lower() for i in string if i.isalnum()]
        return string == string[::-1]


if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    sol4 = Solution4()

    print(sol1.run(string))
    print(sol2.run(string))
    print(sol3.run(string))
    print(sol4.run(string))
