class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num != 1:
            if num % 2 == 0:
                num /= 2
                continue
            elif num % 3 == 0:
                num /= 3
                continue
            elif num % 5 == 0:
                num /= 5
                continue
            return False
        return True
