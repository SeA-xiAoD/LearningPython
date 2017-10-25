class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) >= len(num2):
            long_s = num1
            long_length = len(num1) - 1
            short_s = num2
            short_length = len(num2) - 1
        else:
            long_s = num2
            long_length = len(num2) - 1
            short_s = num1
            short_length = len(num1) - 1
        result = ''
        carry = 0
        while short_length >= 0:
            temp_sum = ord(long_s[long_length]) + ord(short_s[short_length]) + carry - 2 * ord('0')
            if temp_sum > 9:
                carry = 1
                result += str(temp_sum % 10)
            else:
                carry = 0
                result += str(temp_sum)
            short_length -= 1
            long_length -= 1
        while long_length >= 0:
            temp_sum = ord(long_s[long_length]) + carry - ord('0')
            if temp_sum > 9:
                carry = 1
                result += str(temp_sum % 10)
            else:
                carry = 0
                result += str(temp_sum)
            long_length -= 1
        if carry == 1:
            result += '1'
        return result[::-1]
