class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]
        time_list = []
        for hour in range(0, 12):
            for minute in range(0, 60):
                temp_time = ''
                if (bin(hour) + bin(minute)).count('1') == num:
                    if minute < 10:
                        temp_time = str(hour) + ':' + str(0) + str(minute)
                    else:
                        temp_time = str(hour) + ':' + str(minute)
                    time_list.append(temp_time)
        return time_list
