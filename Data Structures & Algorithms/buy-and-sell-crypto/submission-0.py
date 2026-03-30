class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Compute the lowest till date.
        # For each day compute the max profit if we sell today provided that we brought that day.
        lowest_till_today = prices[0]
        max_profit = 0
        for price in prices[1:]:
            profit = price - lowest_till_today
            max_profit = max(max_profit,profit)
            lowest_till_today = min(price,lowest_till_today)
        
        return max_profit