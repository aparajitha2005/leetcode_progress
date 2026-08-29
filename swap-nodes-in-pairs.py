# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0,head)
        prev = dummy
        curr = head
        while curr and curr.next:
            #save ptrs
            nxtpair = curr.next.next
            second = curr.next
            #reverse ptrs
            second.next = curr
            curr.next = nxtpair
            prev.next = second
            #update ptrs
            prev = curr
            curr = nxtpair
        return dummy.next           
            
        # return new head

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        