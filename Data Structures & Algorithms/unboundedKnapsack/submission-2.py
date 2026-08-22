class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity

        prevRow = [0]*(n+1)

        for i in range(m):
            curRow = [0]*(n+1)
            for W in range(1, n+1):
                skip = prevRow[W]

                include = 0 # Use float('-inf') if you have -ve profits
                remainingCapacity = W - weight[i]
                if remainingCapacity >= 0:
                    include = profit[i] + curRow[remainingCapacity]

                curRow[W] = max(include, skip)
            prevRow = curRow

        return prevRow[n]
