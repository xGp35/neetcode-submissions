class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity

        prevRow = [0]*(n+1)

        for i in range(m):
            curRow = [0]*(n+1)
            for W in range(1, n+1):
                include = 0 # Use float('-inf') if you have -ve profits
                if  W  >= weight[i]:
                    include = profit[i] + curRow[W - weight[i]]

                curRow[W] = max(prevRow[W], include)
            prevRow = curRow

        return prevRow[n]
