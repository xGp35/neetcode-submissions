class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(target):
            if target in memo: return memo[target]
            if target == 0: return 0
            if target < 0: return None

            minCoins = float('inf')

            for num in coins:
                remainder = target - num
                remainderResult = dfs(remainder)
                if remainderResult is not None:
                    minCoins = min(minCoins, 1 + remainderResult)
            
            memo[target] = minCoins
            return minCoins
        
        res = dfs(amount)
        return res if res < float('inf') else -1
                    
