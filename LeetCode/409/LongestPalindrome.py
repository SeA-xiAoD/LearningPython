class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        count = 0
        word_list = {}
        for i in range(0, length):
            if s[i] in word_list:
                word_list[s[i]] += 1
            else:
                word_list[s[i]] = 1
        have_odd = 0
        for w in word_list:
            if word_list[w] % 2 == 0:
                count += word_list[w]
            else:
                have_odd = 1
                count += word_list[w] - 1
        return count + have_odd
