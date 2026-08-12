class Solution(object):
    def maxArea(self, height):
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            currarea = min(height[left],height[right])* width 
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            if currarea > maxarea:
                maxarea = currarea
        return maxarea
                
                

        """
        :type height: List[int]
        :rtype: int
        """
        