class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dfs(i, ability_to_buy_state):
            if (i, ability_to_buy_state) in memo: return memo[(i, ability_to_buy_state)]
            if i >= len(prices): return 0

            profit = 0
            if ability_to_buy_state:
                buy = dfs(i+1, not ability_to_buy_state) - prices[i]
                cooldown = dfs(i+1, ability_to_buy_state)
                profit = max(buy,cooldown)
            else:
                sell = dfs(i+2, not ability_to_buy_state) + prices[i]
                # Here we are just changing the state, don't worry too much about it.
                cooldown = dfs(i+1, ability_to_buy_state)
                profit = max(sell,cooldown)

            memo[(i, ability_to_buy_state)] = profit
            return profit
        
        return dfs(0, True)


            