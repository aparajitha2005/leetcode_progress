class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        leftbias = self.rotated(nums , target , True)
        rightbias = self.rotated(nums , target , False)
        return [leftbias , rightbias]
    def rotated(self ,nums,target ,bias):
        l , r = 0 , len(nums) - 1
        i = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                i = mid
                if bias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i  
        
