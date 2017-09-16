class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)

# 125为例，125 100 75 50 25都有两个因子5
