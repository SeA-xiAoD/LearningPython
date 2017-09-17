# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        while head.val == val:
            head = head.next
            if head == None:
                return head
        p = head
        q = p.next
        if q == None:
            if p.val == val:
                return None
            else:
                return head
        while q != None:
            if q.val == val:
                p.next = q.next
            else:
                p = q
            q = q.next
        return head
