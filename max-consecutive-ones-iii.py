class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zero = 0
        maxlength = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            if zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1              
            length = right - left + 1
            if length > maxlength:
                maxlength = length
        return maxlength

