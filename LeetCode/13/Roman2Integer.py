class Solution(object):
    def romanToInt(self, s):
        char_set = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        s_sum = 0
        temp_sum = 0 # to sum if the number is equal to last number

        if(len(s) == 1):
            return char_set[s[0]]

        for i in range(0,len(s)):
            if i == 0:
                temp_sum += char_set[s[i]]
            elif s[i] == s[i-1]:
                temp_sum += char_set[s[i]]
            elif char_set[s[i]] > char_set[s[i-1]]:
                s_sum -= temp_sum
                temp_sum = char_set[s[i]]
            elif char_set[s[i]] < char_set[s[i-1]]:
                s_sum += temp_sum
                temp_sum = char_set[s[i]]

            if i == len(s)-1:
                s_sum += temp_sum

        return s_sum
