class Solution(object):
    def removeDuplicates(self, nums):
        curr = 0
        scan = 0
        if len(nums)== 0:
            return 0
        while scan < len(nums) and curr <= scan:
            if nums[curr] == nums[scan]:
                scan += 1
            else:
                nums[curr + 1] = nums[scan]
                curr += 1
                scan += 1
        return curr + 1
        """
        :type nums: List[int]
        :rtype: int
        """
        