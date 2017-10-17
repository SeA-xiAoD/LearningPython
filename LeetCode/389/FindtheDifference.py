class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        remain_word_dir = {}
        for i in range(0, len(s)):
            if s[i] in remain_word_dir:
                remain_word_dir[s[i]] += 1
            else:
                remain_word_dir[s[i]] = 1
        for i in range(0, len(t)):
            if t[i] in remain_word_dir:
                if remain_word_dir[t[i]] == 0:
                    return t[i]
                else:
                    remain_word_dir[t[i]] -= 1
            else:
                return t[i]
