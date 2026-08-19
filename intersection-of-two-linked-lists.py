# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        nodea = headA
        nodeb = headB
        while nodea != nodeb:
            if nodea is None:
                nodea = headB
            else:
                nodea = nodea.next
            if nodeb is None:
                nodeb = headA
            else:
                nodeb = nodeb.next
        return nodea
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        