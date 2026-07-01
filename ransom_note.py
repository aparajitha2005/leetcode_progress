class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mapcount = {}
        for i in magazine:
            if i in mapcount:
                mapcount[i] +=1
            else:
                mapcount[i] = 1

        for j in ransomNote:
            if j in mapcount and mapcount[j]>0 :
                mapcount[j] -=1
            else:
                return False
        return True


        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        