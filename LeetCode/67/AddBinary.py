class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        l1 = len_a - 1
        l2 = len_b - 1
        carry = 0
        s = ''
        while l1 >= 0 and l2 >= 0:
            temp = int(a[l1]) + int(b[l2]) + carry
            if temp >= 2:
                s = str(temp%2) + s
                carry = 1
            else:
                s = str(temp) + s
                carry = 0
            l1 -= 1
            l2 -= 1

        if l1 == -1:
            while l2 >= 0:
                temp = int(b[l2]) + carry
                if temp >= 2:
                    s = str(temp%2) + s
                    carry = 1
                else:
                    s = str(temp) + s
                    carry = 0
                l2 -= 1

        elif l2 == -1:
            while l1 >= 0:
                temp = int(a[l1]) + carry
                if temp >= 2:
                    s = str(temp%2) + s
                    carry = 1
                else:
                    s = str(temp) + s
                    carry = 0
                l1 -= 1

        if carry == 1:
            s = '1' + s
        return s
