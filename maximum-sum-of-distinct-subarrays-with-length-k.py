class Solution(object):
    def maximumSubarraySum(self, nums, k):
        windowsum = 0
        left = 0
        right = k - 1
        maxsum = windowsum
        freq = {}
        for i in range(k):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        windowsum = sum(nums[:k])
        while right < len(nums) and left <= right:
            if len(freq) == k:
                if windowsum > maxsum:
                    maxsum = windowsum
            if right == len(nums) - 1:
                break
            windowsum -= nums[left]
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
            right +=1
            windowsum += nums[right]
            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1

        return maxsum
                

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        