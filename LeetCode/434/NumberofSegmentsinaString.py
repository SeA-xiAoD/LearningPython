class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        p = 0
        count = 0
        while p < length:
            tag = 0
            while p < length and s[p] == ' ':
                p += 1
            while p < length and s[p] != ' ':
                tag = 1
                p += 1
            if tag == 1:
                count += 1
        return count
