class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        r = 0
        for i in points:
            temp_dir = {}
            for j in points:
                dis = (i[0]-j[0])*(i[0]-j[0]) + (i[1]-j[1])*(i[1]-j[1])
                if dis in temp_dir:
                    r += temp_dir[dis] * 2
                    temp_dir[dis] += 1
                else:
                    temp_dir[dis] = 0
        return r
