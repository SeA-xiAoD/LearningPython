class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        for i in range(0, 32):
            r <<= 1
            # get the last bit and put on the right of r
            r |= n & 1
            n >>= 1
        return r
