class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        left = 0
        right = k-1
        count = 0
        windowsum = sum(arr[:k])
        while right < len(arr) and left <= right:
            if float(windowsum)/k >= threshold:
                count += 1
            if right <= len(arr) - 2:
                windowsum -= arr[left]
                left += 1
                right += 1
                windowsum += arr[right]
            else:
                break
        return count 
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        