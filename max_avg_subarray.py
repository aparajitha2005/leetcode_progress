class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        right = k-1
        windowsum = sum(nums[:k])
        maxsum = windowsum
        while right < len(nums)-1 and left <= right:
            
            windowsum -= nums[left]
            left += 1
            right += 1
            windowsum += nums[right]
            if windowsum > maxsum:
                maxsum = windowsum
        return float(maxsum)/k
            

        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        