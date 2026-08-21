class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity

        prevRow = [0]*(n+1)

        for col in range(n+1):
            if col - weight[0] >= 0:
                prevRow[col] = profit[0]
        

        for i in range(1,m):
            curRow = [0]*(n+1)
            for W in range(1,n+1): # W is the current capacity we are considering
                # decision to skip ith element
                skip = prevRow[W]

                # decision to take it
                include = 0   # initialize to zero becz we may decide to skip it
                remainingCapacity = W - weight[i]
                if remainingCapacity >= 0:
                    include = profit[i] + prevRow[remainingCapacity]
                
                curRow[W] = max(skip, include)
            prevRow = curRow
        
        return prevRow[n]


        
