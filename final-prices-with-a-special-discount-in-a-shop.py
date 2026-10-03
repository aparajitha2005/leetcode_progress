class Solution(object):
    def finalPrices(self, prices):
        stack = []
        res = prices[:]
        for i in range(len(prices)):
            curr = prices[i]
            while stack and curr <= prices[stack[-1]]:
                val = stack.pop()
                res[val] = prices[val] - prices[i]
            stack.append(i)
        return res
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        
