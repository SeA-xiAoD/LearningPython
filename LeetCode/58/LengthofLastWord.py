class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length1 = 0
        length2 = 0
        if len(s) == 0:
            return 0
        k = 0
        while k < len(s):
            if s[k] != ' ':
                length1 += 1
            elif length1 != 0: # s[k]==' ' and s[k-1] == ' ' so not change l2
                length2 = length1
                length1 = 0
            k += 1
        if length1 != 0:
            return length1
        else:
            return length2
