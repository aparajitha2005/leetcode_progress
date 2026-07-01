class Solution(object):
    def reverseString(self, s):
        first = 0
        end = len(s) - 1
        while first < end:
	        temp = s[first]
	        s[first] = s[end]
	        s[end] = temp
	        first+=1
	        end-=1
        return s



        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        