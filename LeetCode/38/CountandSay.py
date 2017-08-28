class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        init = '11'
        if n == 2:
            return init
        k = 2 # count number to n
        while k < n:
            i = 0 # count number in init
            length = len(init)
            say = ''
            count = 0
            now_word = init[0]
            while i < length:
                if now_word == init[i]:
                    count += 1
                else:
                    say += str(count) + init[i-1]
                    now_word = init[i]
                    count = 1
                i += 1
            say += str(count) + init[length-1]
            init = say
            k += 1
        return say
