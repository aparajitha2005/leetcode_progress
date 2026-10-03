class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]
        for i in s:
            if i == '(':
                stack.append(0)
            if i == ')':
                pop = stack.pop()
                if pop == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2*pop
        return stack[-1]

        """
        :type s: str
        :rtype: int
        """
        
