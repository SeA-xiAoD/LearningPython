# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = n // 2
        max_number = n
        min_number = 1
        guess_result = guess(number)
        while guess_result != 0:
            if guess_result == 1:
                min_number = number + 1
                number = number + (max_number - number) // 2 + 1
                guess_result = guess(number)
            elif guess_result == -1:
                max_number = number - 1
                number = number // 2
                guess_result = guess(number)
        return number
