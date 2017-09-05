class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True
        new_s = s.lower()
        l = 0
        r = len(new_s)-1
        while l < r:
            if new_s[l].isalpha() == False and new_s[l].isdigit() == False:
                l += 1
                continue
            if new_s[r].isalpha() == False and new_s[r].isdigit() == False:
                r -= 1
                continue
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True
