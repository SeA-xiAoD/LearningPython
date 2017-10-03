class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_dir = {}
        for letter in s:
            try:
                letter_dir[letter] += 1
            except:
                letter_dir[letter] = 1
        for letter in t:
            try:
                letter_dir[letter] -= 1
            except:
                return False
        for key in letter_dir:
            if letter_dir[key] != 0:
                return False
        return True
