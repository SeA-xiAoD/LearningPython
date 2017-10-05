class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words_list = str.split(' ')
        length = len(pattern)
        match_dir = {}
        words_set = set()
        if length != len(words_list):
            return False
        for i in range(0, length):
            try:
                if match_dir[pattern[i]] != words_list[i]:
                    return False
            except:
                if words_list[i] not in words_set:
                    match_dir[pattern[i]] = words_list[i]
                    words_set.add(words_list[i])
                else:
                    return False
        return True
