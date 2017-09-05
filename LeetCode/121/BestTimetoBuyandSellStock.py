class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_profit = 0
        min_price = prices[0]
        for p in prices:
            if p - min_price > max_profit:
                max_profit = p - min_price
            if p < min_price:
                min_price = p
        return max_profit
