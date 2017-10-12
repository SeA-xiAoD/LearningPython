class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        max_int = 0x7FFFFFFF
        all_1 = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & all_1, ((a & b) << 1) & all_1
            # 前半段是不进位的加计算，后半段是进位的计算
        return a if a <= max_int else ~(a ^ all_1)
