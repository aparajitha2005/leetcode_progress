class Solution(object):
    def decodeString(self, s):
        stack = []
        for i in s:
            if i!= ']':
                stack.append(i)
            else:
                sub = ''
                while stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop()
                
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*sub)
        return "".join(stack)

        """
        :type s: str
        :rtype: str
        """
        
