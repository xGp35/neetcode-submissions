class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        memo = {}
        # Return the minimum number of coins needed to make target
        def helper(target):
            if target in memo: return memo[target]
            if target < 0: return None
            if target == 0: return 0

            minCoins = float('inf')
            for coin in coins:
                remainder = target - coin
                remainderResult = helper(remainder)
                if remainderResult is not None:
                    minCoins = min(minCoins, 1 + remainderResult)
            memo[target] = minCoins
            return minCoins

        ans = helper(amount)
        return ans if ans < float('inf') else -1
