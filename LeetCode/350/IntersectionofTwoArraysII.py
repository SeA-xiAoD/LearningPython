class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        number_count1 = {}
        number_count2 = {}
        for number in nums1:
            try:
                number_count1[number] += 1
            except:
                number_count1[number] = 1
        for number in nums2:
            try:
                number_count2[number] += 1
            except:
                number_count2[number] = 1
        r_list = []
        number_count1_key = number_count1.keys()
        for key in number_count1_key:
            try:
                count1 = number_count1[key]
                count2 = number_count2[key]
                if count1 < count2:
                    for i in range(0, count1):
                        r_list.append(key)
                else:
                    for i in range(0, count2):
                        r_list.append(key)
            except:
                continue
        return r_list
