class Solution(object):
    def backspaceCompare(self, s, t):
        stacks = []
        for i in s:
            if stacks and i == '#':
                stacks.pop()
            elif not stacks and i == '#':
                continue
            else:
                stacks.append(i)
        ss = "".join(stacks)
        stackt = []
        for i in t:
            if stackt and i == '#':
                stackt.pop()
            elif not stackt and i == '#':
                continue
            else:
                stackt.append(i)
        tt = "".join(stackt)
        if ss == tt:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
