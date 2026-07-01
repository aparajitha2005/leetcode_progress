class Solution(object):
    def intersection(self, nums1, nums2):
        output = []
        set1 = set()
        for i in nums1:
	        set1.add(i)
        for j in nums2:
	        if j in set1:
		        output.append(j)
                set1.discard(j)
        return output
		



        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        