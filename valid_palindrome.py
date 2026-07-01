
	
class Solution(object):
    def isPalindrome(self, s):
        first = 0
        end = len(s) - 1

        while first < end:

            if s[first].isalnum() is False:
                first += 1

            if s[end].isalnum() is False:
                end -= 1

            if s[first].isalnum() and s[end].isalnum():
                if s[first].lower() != s[end].lower():
                    return False
                else:
                    first += 1
                    end -= 1

        return True

        
       





		