"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


class Solution1(object):
    def run(self, prices: list[int]) -> int:
        maxdiff = 0

        for buy_index in range(len(prices) - 1):
            for sell_index in range(buy_index + 1, len(prices)):
                diff = prices[sell_index] - prices[buy_index]
                if diff > maxdiff:
                    maxdiff = diff

        return maxdiff


class Solution2(object):
    """
    Kadane's Algorithm

    916 ms, 27.2 MB

    """

    def run(self, prices: list[int]) -> int:
        maxCur = 0
        maxSoFar = 0

        for index in range(1, len(prices)):
            maxCur = max(0, maxCur + prices[index] - prices[index - 1])
            maxSoFar = max(maxCur, maxSoFar)
            index += 1

        return maxSoFar


class Solition3(object):
    """
    870 ms, 27.2 MB
    """

    def run(self, prices: list[int]) -> int:
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


if __name__ == "__main__":
    prices = [1, 4, 2, 6]

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solition3()

    sol1.run(prices)
    sol2.run(prices)
    sol3.run(prices)
