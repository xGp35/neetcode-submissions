class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity

        prevRow = [0]*(n+1)

        for W in range(n+1):
            if W - weight[0] >= 0:
                prevRow[W] = profit[0] + prevRow[W-weight[0]]

        for i in range(1, m):
            curRow = [0]*(n+1)
            for W in range(1, n+1):
                #skip
                skip = prevRow[W]

                #take
                include = 0 # Use float('-inf') if you have -ve profits
                remainingCapacity = W - weight[i]
                if remainingCapacity >= 0:
                    include = profit[i] + curRow[remainingCapacity]

                curRow[W] = max(include, skip)
            prevRow = curRow

        return prevRow[n]
