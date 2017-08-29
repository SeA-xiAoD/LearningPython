# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p = head.next
        q = head
        while p != None:
            if p.val == q.val:
                q.next = p.next
            else:
                q = p
            p = p.next
        return head
