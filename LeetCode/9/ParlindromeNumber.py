class Solution(object):
    def isPalindrome(self, x):
        if(x < 0):
            return False
        numbers = []
        n_numbers = 0
        while(x != 0):
            numbers.append(x % 10)
            x //= 10
            n_numbers += 1
        l = 0
        r = n_numbers-1
        while(l <= r):
            if(numbers[l] != numbers[r]):
                return False
            else:
                l += 1
                r -= 1
                continue
        return True
