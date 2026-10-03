class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        res = [-1]*len(nums)
        for i in range(2*len(nums)):
            curr = nums[i%len(nums)]
            while stack and curr > nums[stack[-1]]:
                val = stack.pop()
                res[val] = curr
            if i < len(nums):
                stack.append(i%len(nums))
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
