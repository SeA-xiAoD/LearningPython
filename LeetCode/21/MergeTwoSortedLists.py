# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1

        p = l1
        q = l2
        k = ListNode(0) # head node
        head = k

        while p != None and q != None:
            if p.val <= q.val:
                k.next = p
                p = p.next
                k = k.next
            elif p.val > q.val:
                k.next = q
                q = q.next
                k = k.next
        while p != None:
            k.next = p
            p = p.next
            k = k.next
        while q != None:
            k.next = q
            q = q.next
            k = k.next

        return head.next
