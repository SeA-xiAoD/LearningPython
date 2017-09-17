class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        while n != 1:
            s = 0
            while n != 0:
                s += (n % 10) ** 2
                n //= 10
            n = s
            try:
                if dic[n] == 1:
                    break
            except:
                dic[n] = 1
        return n == 1
