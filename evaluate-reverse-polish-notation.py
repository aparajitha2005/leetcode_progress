class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == '+':
                result = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif i == '*':
                result = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(result) 
            elif i == "-":
                result = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif i == "/":
                result = int(float(stack[-2]) / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[-1]               
                
        """
        :type tokens: List[str]
        :rtype: int
        """
        
