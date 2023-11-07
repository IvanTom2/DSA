"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
"""


class Solution1(object):
    """
    45 ms, 16.3 MB
    """

    def run(self, num1: str, num2: str) -> str:
        ind1 = len(num1) - 1
        ind2 = len(num2) - 1
        num = []
        carry = 0

        while ind1 >= 0 or ind2 >= 0 or carry:
            d1 = int(num1[ind1]) if ind1 >= 0 else 0
            d2 = int(num2[ind2]) if ind2 >= 0 else 0

            num += [str((d1 + d2 + carry) % 2)]
            carry = (d1 + d2 + carry) // 2

            ind1 -= 1
            ind2 -= 1

        return "".join(num[::-1])


class Solution2(object):
    """
    37 ms, 16.3 MB
    """

    def run(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(num1[i]) - ord("0")
            if j >= 0:
                sum += ord(num2[j]) - ord("0")
            i, j = i - 1, j - 1
            carry = 1 if sum > 1 else 0
            res += str(sum % 2)

        if carry != 0:
            res += str(carry)
        return res[::-1]


if __name__ == "__main__":
    num1, num2 = "11", "1"

    sol = Solution1()
    print(sol.run(num1, num2))
