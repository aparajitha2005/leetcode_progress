class Solution(object):
    def isAnagram(self, s, t):
        count = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for j in t:
            if j in count:
                count[j] -= 1
            else:
                return False

        
        for value in count.values():
            if value != 0:
                return  False
        return True 
       