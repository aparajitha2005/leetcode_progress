class Solution(object):
    def isSubsequence(self, s, t):
        ps = 0
        pt = 0
        if len(s) == 0:
            return True
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                # a match
                ps +=1
            pt += 1
        if ps == len(s):
            return True
        else:
            return False
        


       
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        