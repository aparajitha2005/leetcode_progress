class Solution(object):
    def removeElement(self, nums, val):
        curr = 0
        scan = 0
        if len(nums) == 0:
            return 0
        while scan < len(nums):
            if nums[scan] != val:
                nums[curr] = nums[scan]
                curr +=1
                scan +=1

            else:
                while scan < len(nums) and nums[scan] == val:
                    scan += 1
               
        return curr  

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        