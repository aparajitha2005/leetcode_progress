class Solution(object):
    def simplifyPath(self, path):
        stack = []
        parts = path.split('/')
        for i in parts:
            if i == '.':
               #return top
                continue
            elif stack and i == '..':
                stack.pop()
            elif not stack and i == "..":
                continue
            elif i:
                stack.append(i)
        return "/"+"/".join(stack)        
            
        """
        :type path: str
        :rtype: str
        """
        
