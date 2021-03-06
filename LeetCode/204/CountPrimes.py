from math import sqrt

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, int(sqrt(n)) + 1):
            if res[i] == True:
                for j in range(2, (n-1)//i+1):
                    # start from 2 to avoid primes
                    res[i*j] = False
        return sum(res)
