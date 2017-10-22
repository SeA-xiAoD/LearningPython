class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r_list = []
        for number in range(1, n + 1):
            if number % 3 == 0 and number % 5 == 0:
                r_list.append('FizzBuzz')
            elif number % 3 == 0:
                r_list.append('Fizz')
            elif number % 5 == 0:
                r_list.append('Buzz')
            else:
                r_list.append(str(number))
        return r_list
