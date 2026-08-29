# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None:
            return None
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        mod = k%count
        if mod == 0:
            return head
        curr = head
        for i in range(count - mod - 1):
            curr = curr.next
        first , newhead = curr.next , curr.next
        curr.next = None
        while first.next:
            first = first.next
        first.next = head
        return  newhead

        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        