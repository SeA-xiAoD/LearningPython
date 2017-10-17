class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        k = 1 # the bit of the number in now position
        temp_n = n
        remain = n
        while temp_n > 0:
            remain = temp_n
            temp_n -= 9 * (10 ** (k - 1)) * k
            k += 1
        k -= 1
        now_bit = remain % k # get the char's position in now number
        if now_bit == 0:
            now_position = remain // k # get now position in now length of number
        else:
            now_position = remain // k + 1
        sum_now = 10 ** (k-1) + now_position - 1
        print(now_position)
        print(sum_now)
        return int(str(sum_now)[now_bit - 1])
