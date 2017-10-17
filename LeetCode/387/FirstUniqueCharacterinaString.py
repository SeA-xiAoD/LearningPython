class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_count = {}
        length = len(s)
        if length == 0:
            return -1
        for i in range(0, length):
            if s[i] in word_count:
                word_count[s[i]][1] += 1
            else:
                word_count[s[i]] = [i, 1]
        now_first_position = 0x7FFFFFFF
        keys = word_count.keys()
        keys = list(keys)
        for i in range(0, len(keys)):
            if word_count[keys[i]][1] == 1:
                if word_count[keys[i]][0] < now_first_position:
                    now_first_position = word_count[keys[i]][0]
        if now_first_position == 0x7FFFFFFF:
            now_first_position = -1
        return now_first_position
