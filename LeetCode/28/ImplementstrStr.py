class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_needle = len(needle)
        length_haystack = len(haystack)
        if length_needle == 0 and length_haystack == 0:
            return 0
        if length_needle > length_haystack:
            return -1

        k = 0
        dis = length_haystack - length_needle
        find = 0
        while k <= dis and find == 0:
            find = 1
            for i in range(0, length_needle):
                if haystack[k+i] != needle[i]:
                    find = 0
                    k += 1
                    break

        if find == 0:
            return -1
        elif find == 1:
            return k
