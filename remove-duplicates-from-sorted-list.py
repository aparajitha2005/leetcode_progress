# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        tail = head
        while tail and tail.next:
            if tail.val == tail.next.val:
                tail.next = tail.next.next
            else:
                tail = tail.next
        return head
                     

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        