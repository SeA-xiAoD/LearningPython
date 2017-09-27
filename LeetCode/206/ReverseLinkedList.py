# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p = head
        q = head.next
        head.next = None
        r = head
        while q != None:
            p = q
            q = q.next
            p.next = r
            r = p
        head = p
        return head
