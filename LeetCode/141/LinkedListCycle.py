# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        if head.next == None:
            return False
        fast = head.next
        slow = head
        while fast != slow and fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return fast == slow
