# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        stack = []
        arr = []
        ptr = head
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        res = [0]*len(arr)
        for i in range(len(arr)):
            curr = arr[i]
            while stack and curr > arr[stack[-1]]:
                ind = stack.pop()
                res[ind] = curr
            stack.append(i)
        return res



        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        
