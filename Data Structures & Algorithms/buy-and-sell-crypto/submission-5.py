class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l = r
            maxProfit = max(maxProfit, profit)
            r+=1
        
        return maxProfit