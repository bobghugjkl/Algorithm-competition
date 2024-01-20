# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        a = head
        b = head.next
        a.next = None
        while b:
            c = b.next
            b.next = a
            a,b = b,c
        return a
            
        
