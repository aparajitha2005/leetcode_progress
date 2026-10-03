class Solution(object):
    def calculate(self, s):
        stack = []
        prevop = '+'
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in '+*/-' or i == len(s) - 1:
                if prevop == '+':
                    stack.append(num)
                elif prevop == '-':
                    stack.append(-num)
                elif prevop == '*':
                    stack.append(stack.pop()*num)
                elif prevop == '/':
                    stack.append(int(float(stack.pop())/num))
                if s[i] in '+/-*':
                    prevop = s[i]
                num = 0
        return sum(stack)
                

            

        """
        :type s: str
        :rtype: int
        """
        
