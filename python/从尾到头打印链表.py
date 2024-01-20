# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def printListReversingly(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        p = head
        while p:
            res.append(p.val)
            p = p.next
        return res[::-1]
