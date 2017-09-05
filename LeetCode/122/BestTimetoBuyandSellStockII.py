class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        min_price = prices[0]
        max_price = prices[0]
        price_sum = 0
        flag = 0 # 0:find min, 1:find max
        for p in prices:
            if flag == 0:
                if p <= min_price:
                    min_price = p
                else:
                    max_price = p
                    flag = 1
            elif flag == 1:
                if p >= max_price:
                    max_price = p
                else:
                    price_sum += max_price - min_price
                    min_price = p
                    flag = 0
        if flag == 1:
            price_sum += max_price - min_price
        return price_sum
