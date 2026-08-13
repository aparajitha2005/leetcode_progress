class Solution(object):
    def maxVowels(self, s, k):
        left = 0
        right = k - 1
        windowlen = len(s[:k])
        count = 0
        for i in range(windowlen):
            if s[i] in "aeiou":
                count += 1
        maxcount = count
        while right < len(s) - 1 and left <= right:
            if s[left] in "aieou":
                count -= 1
            left += 1
            right += 1
            if s[right] in "aieou":
                count += 1
            if count > maxcount:
                maxcount = count
        return maxcount

            

           

        """
        :type s: str
        :type k: int
        :rtype: int
        """
        