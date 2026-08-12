class Solution(object):
    def sortedSquares(self, nums):
        first = 0
        end = len(nums) - 1
        output = []
        while first <= end:
            if abs(nums[first]) < abs(nums[end]):
                output.append(nums[end]**2)
                end -=1
            else:
                output.append(nums[first]**2)
                first +=1
        output.reverse()
        return output


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        