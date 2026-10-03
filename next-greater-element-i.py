class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nums1idx =  {n : i for i , n in enumerate(nums1)}
        stack = []
        res = [-1]*len(nums1)
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                index = nums1idx[val]
                res[index] = curr
            if curr in nums1idx:
                stack.append(curr)
            
        return res    

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
