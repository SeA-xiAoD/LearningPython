class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        r_list = [[1]]
        for i in range(1, numRows):
            r_list.append([])
            r_list[i].append(1)
            r_list[i].append(1)
            for j in range(1, i):
                r_list[i].insert(j, r_list[i-1][j-1] + r_list[i-1][j])
        return r_list
