# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        dec = 0
        while head:
            dec = dec*2 + head.val
            head = head.next
        return dec
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        