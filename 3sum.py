class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            if i>0 and nums[i-1] == nums[i]:
                    continue
            while start < end:
                    if nums[start] + nums[end] < -(nums[i]):
                        start +=1
                    elif nums[start] + nums[end] > -(nums[i]):
                        end -=1
                    elif nums[start] + nums[end] == -(nums[i]):
                        result.append([nums[i],nums[start],nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start-1] == nums[start]:
                            start +=1
                        while start < end and end < len(nums) -1 and nums[end+1] ==     nums[end]:
                            end -=1    
        return result


        


        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        