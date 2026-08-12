class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set()
        output = []
        nums2set = set(nums2)
        
            
        for i in nums1:
            if i in nums2set:
                seen.add(i)
          
        output = list(seen)
        return output

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        