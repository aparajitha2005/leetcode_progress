class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = (n*(n+1))//2
        target = total - sum(nums)
        return target
		
        """
        :type nums: List[int]
        :rtype: int
        """
        