class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        count = 0
        other_count = 0
        now_pos = 0 # start from right
        while now_pos < 31:
            if now_pos % 2 == 0:
                count += num & 1
            else:
                other_count += num & 1
            num >>= 1
            now_pos += 1
        return count == 1 and other_count == 0
