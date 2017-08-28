class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[len(digits)-1] < 9:
            digits[len(digits)-1] += 1
            return digits
        else:
            carry = 1
            k = len(digits) - 1
            while k >= 0 and carry == 1:
                digits[k] += 1
                if digits[k] == 10:
                    digits[k] = 0
                    carry = 1
                    k -= 1
                else:
                    carry = 0
            if carry == 1:
                digits.insert(0, 1)
            return digits
