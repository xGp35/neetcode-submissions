class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        idx_day_map = {0: 1, 1: 7, 2:30}
        memo = {}

        def find_next_i(k, days_pass):
            coverage_till = days[k] + days_pass - 1
            while k<n and coverage_till >= days[k]:
                k += 1
            return k

        # i is the next day which is not covered so far
        def dfs(i):
            if i in memo: return memo[i]
            if i >= n: return 0 # If all days covered, no more cost

            minCost = float('inf')

            for j, cost in enumerate(costs):
                days_pass = idx_day_map[j]
                next_i = find_next_i( i, days_pass)
                minCost = min(minCost, cost + dfs(next_i))
            memo[i] = minCost
            return minCost
            
        return dfs(0)
                
