# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        p = headA
        length_A = 0
        while p != None:
            length_A += 1
            p = p.next
        p = headB
        length_B = 0
        while p != None:
            length_B += 1
            p = p.next
        p = headA
        while length_A > length_B:
            p = p.next
            length_A -= 1
        q = headB
        while length_B > length_A:
            q = q.next
            length_B -= 1
        while p != q:
            p = p.next
            q = q.next
        return p
