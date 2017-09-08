class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        numbers = []
        while n > 0:
            numbers.insert(0, (n-1)%26)
            n = (n-1) // 26
        tag = ''
        print(numbers)
        for n in numbers:
            tag += chr(ord('A') + n)
        return tag
