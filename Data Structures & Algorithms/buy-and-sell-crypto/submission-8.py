class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_price = prices[0]
        for price in prices:
            maxP = max(maxP, price - min_price)
            min_price = min(price, min_price)
        return maxP