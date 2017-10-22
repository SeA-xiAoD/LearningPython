class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        bits = [0] * 32
        temp = '0123456789abcdef'
        temp_n = num
        bit_number = list(temp)
        r = ''
        if num > 0:
            for i in range(31, -1, -1):
                bits[i] = temp_n & 1
                temp_n >>= 1
        else:
            temp_n = abs(num) - 1
            for i in range(31, -1, -1):
                bits[i] = ~temp_n & 1
                temp_n >>= 1
        for i in range(0, 32, 4):
            s = 0
            s += 8 * bits[i]
            s += 4 * bits[i + 1]
            s += 2 * bits[i + 2]
            s += 1 * bits[i + 3]
            if s == 0 and len(r) != 0:
                r += bit_number[s]
            elif s != 0:
                r += bit_number[s]
        return r
