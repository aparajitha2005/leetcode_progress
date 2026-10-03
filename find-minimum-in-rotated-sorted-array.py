class Solution:
    def findMin(self, nums: list[int]) -> int:
        left , right = 0 , len(nums) - 1
        res = nums[0]
        while left <= right:
            if nums[left] <= nums[right]:
                return min(res , nums[left])
            mid = (left + right)//2
            res = min(nums[mid], nums[left])
            if nums[mid] >= nums[left]:
                left = mid + 1  
            else:
                right = mid - 1
        return res
            
