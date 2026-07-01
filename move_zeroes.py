class Solution(object):
    def moveZeroes(self, nums):
        curr = 0
        next = 1
        while next < len(nums):
	        if nums[curr] == 0 and nums[next] != 0:
		        nums[curr] , nums[next] = nums[next] , nums[curr]
		        curr +=1
		        next +=1
	        elif  nums[curr] ==0 and nums[next] == 0:
		        while  next < len(nums) and nums[next] == 0:
				        next +=1
	        else:
		
		        curr +=1
		        next +=1
        return nums






        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        