class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return
        length = len(s)
        sum_s = 0
        for i in range(0, length):
            p = length - i - 1
            ascii_dis = ord(s[i]) - ord('A') + 1
            sum_s += ascii_dis * (26 ** p)
        return sum_s
