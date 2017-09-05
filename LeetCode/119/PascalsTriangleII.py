class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        old_list = [1]
        new_list = []
        for i in range(0, rowIndex):
            new_list.append(1)
            new_list.append(1)
            for j in range(0, i):
                new_list.insert(j+1, old_list[j] + old_list[j+1])
            old_list = new_list
            new_list = []
        return old_list
