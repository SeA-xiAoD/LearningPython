class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length_s = len(s)
        length_t = len(t)
        if length_s != length_t:
            return False
        char_in_t = [0] * 256
        char_in_s = [0] * 256
        i = 0
        while i < length_s:
            if char_in_s[ord(s[i])] == 0 and char_in_t[ord(t[i])] == 0:
                char_in_s[ord(s[i])] = ord(t[i])
                char_in_t[ord(t[i])] = ord(s[i])
            else:
                if char_in_s[ord(s[i])] != ord(t[i]) or char_in_t[ord(t[i])] != ord(s[i]):
                    return False
                i += 1
        return True
