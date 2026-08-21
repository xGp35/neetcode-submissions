class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        # This will return the max size subset
        def dfs(i, targ1, targ2):
            # base cases
            if (i,targ1,targ2) in memo: return memo[(i,targ1,targ2)]
            if targ1 < 0 or targ2 < 0: return 0
            if targ1 == 0 and targ2 == 0: return 1
            if i >= len(strs): return 1

            zero_cnt = strs[i].count("0")
            one_cnt = strs[i].count("1")

            # skip
            skip = dfs(i+1, targ1, targ2)

            # take
            take = 1 + dfs(i+1, targ1 - zero_cnt, targ2 - one_cnt)
            
            memo[(i,targ1,targ2)] = max(skip,take)
            return max(skip,take)

        return dfs(0, m , n) - 1