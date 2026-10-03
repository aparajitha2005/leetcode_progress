class Solution(object):
    def dailyTemperatures(self, temperatures):
        tempidx = {n: i for i , n in enumerate(temperatures)}
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and curr > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
                

        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
