class Solution(object):
    def longestSubarray(self, nums):
        left, count, maxlength = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            length = right - left
            if length > maxlength:
                maxlength = length
        return maxlength
        """
        :type nums: List[int]
        :rtype: int
        """
        