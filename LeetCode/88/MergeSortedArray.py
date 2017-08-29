class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = p2 = 0
        if m < len(nums1):
            for i in range(m, len(nums1)):
                nums1.pop(m)
        while p2 < n:
            while p1 < m and nums1[p1] < nums2[p2]:
                p1 += 1
            nums1.insert(p1, nums2[p2])
            p2 += 1
            m += 1
        print(nums1)
