class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Newton method
        r = x
        while r*r > x:
            r = (r + x/r) // 2
        return int(r)
