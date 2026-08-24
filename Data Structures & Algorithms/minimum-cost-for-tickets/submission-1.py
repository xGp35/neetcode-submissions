class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        idx_day_map = {0: 1, 1: 7, 2:30}
        dp = [float('inf')]*(n+1)
        dp[n] = 0

        def find_next_i(k, days_pass):
            coverage_till = days[k] + days_pass - 1
            while k<n and coverage_till >= days[k]:
                k += 1
            return k

        for D in range(n-1, -1, -1):
            for j in range(3):
                days_pass = idx_day_map[j]
                next_i = find_next_i(D, days_pass)
                dp[D] = min(dp[D], costs[j] + dp[next_i])
        
        return dp[0]

        
