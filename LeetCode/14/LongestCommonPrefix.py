class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            for i in range(0,len(strs)):
                if len(strs[i]) == 0:
                    return ''

        min = 2**31-1
        for i in range(0,len(strs)):
            if len(strs[i]) < min:
                min = len(strs[i])
            if len(strs[i]) == 1:
                for j in range(0,len(strs)):
                    if strs[j][0] != strs[i][0]:
                        return ''
                return strs[i]

        k = 0
        flag = 0
        while(flag == 0 and k<min):
            for i in range(1,len(strs)):
                if(strs[i-1][k] != strs[i][k]):
                    flag = 1
            if flag == 0:
                k += 1

        return strs[0][:k]
