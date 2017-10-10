class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowels_set = set(vowels)
        s_list = list(s)
        left = 0
        right = length - 1
        while left < right:
            while left < right and s_list[left] not in vowels_set:
                left += 1
            while left < right and s_list[right] not in vowels_set:
                right -= 1
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return ''.join(s_list)
