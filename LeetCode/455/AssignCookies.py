class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        r = 0
        i = 0
        for size in s:
            if i == len(g):
                break
            if size >= g[i]:
                r += 1
                i += 1
        return r
