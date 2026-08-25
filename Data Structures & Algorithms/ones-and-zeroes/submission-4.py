class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            zero_cnt, one_cnt = s.count("0"), s.count("1")
            for Z in range(m, zero_cnt -1, -1):
                for O in range(n , one_cnt-1, -1):
                    dp[Z][O] = max(dp[Z][O], 1 + dp[Z - zero_cnt][O - one_cnt])
        
        return dp[m][n]
"""
For findMaxForm, you could have:

dp[i][Z][O]

where:

dp[i][Z][O] = maximum number of strings we can choose using the first i strings, with at most Z zeros and O ones.

Then the recurrence is:

dp[i][Z][O] =
    max(
        dp[i-1][Z][O],                         # don't take string i
        1 + dp[i-1][Z-zero][O-one]             # take string i
    )

Notice both transitions come from i-1.

So you can iterate Z and O forward or backward; it doesn't matter for correctness, because you're always reading from the previous item layer.

That's the key.

The backward rule is specifically a consequence of compression
"""