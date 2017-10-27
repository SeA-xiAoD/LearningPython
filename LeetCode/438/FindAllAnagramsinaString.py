class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        length_s = len(s)
        length_p = len(p)
        r = []
        if length_s < length_p:
            return r
        s_hash, p_hash = [0] * 123, [0] * 123
        for i in range(0, length_p):
            p_hash[ord(p[i])] += 1
        for i in range(0, length_p):
            s_hash[ord(s[i])] += 1
        if p_hash == s_hash:
            r.append(0)
        for i in range(1, length_s - length_p + 1):
            s_hash[ord(s[i - 1])] -= 1
            s_hash[ord(s[i + length_p - 1])] += 1
            if s_hash == p_hash:
                r.append(i)
        return r
