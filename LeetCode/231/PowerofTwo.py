class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bi_num = []
        if n < 0:
            return False
        for i in range(0, 32):
            bi_num.append(n & 1)
            n >>= 1
        return sum(bi_num) == 1
