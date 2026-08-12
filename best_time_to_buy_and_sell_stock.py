class Solution(object):
    def maxProfit(self, prices):
        cheap =0
        sell = cheap + 1
        maxprofit = 0
        while sell < len(prices) and cheap < sell:
            if prices[cheap] > prices[sell]:
                cheap = sell
            
            profit = prices[sell] - prices[cheap]
            if profit > maxprofit:
                maxprofit = profit
            sell += 1
        return maxprofit
        """
        :type prices: List[int]
        :rtype: int
        """
        