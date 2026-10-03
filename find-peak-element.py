class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left , right = 0 , len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid 
        return right

        
