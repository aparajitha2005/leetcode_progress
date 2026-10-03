class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l , r = 0 , 0
        maximum1 = 0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            elif s[i] == ')':
                r += 1
            if l == r:
                maximum1 = max(maximum1, l+r)
            elif r > l:
                l = r = 0
        l ,r = 0, 0
        maximum2 = 0
        for i in range(len(s) - 1, - 1,- 1):
            if s[i] == '(':
                l += 1
            elif s[i] == ')':
                r += 1
            if l == r:
                maximum2 = max(maximum2, l+r)
            elif l > r:
                l = r = 0  
        res = max(maximum1 , maximum2)
        return res
