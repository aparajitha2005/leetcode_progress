class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = {}
        left, maxlength = 0 , 0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            while s[right] not in count:
                count[s[right]] = 1
            
            while count[s[right]] > 1:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            length = right - left + 1
            if length > maxlength:
                maxlength = length
        return maxlength
             
        """
        :type s: str
        :rtype: int
        """
        