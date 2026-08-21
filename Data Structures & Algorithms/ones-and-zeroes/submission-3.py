class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        # This will return the max size subset
        def dfs(i, targ1, targ2):
            # base cases
            if (i,targ1,targ2) in memo: return memo[(i,targ1,targ2)]
            if i >= len(strs): return 0

            zero_cnt = strs[i].count("0")
            one_cnt = strs[i].count("1")

            # skip
            skip = dfs(i+1, targ1, targ2)

            # take
            include = 0
            if targ1 - zero_cnt >= 0 and targ2 - one_cnt>=0:
                include = 1 + dfs(i+1, targ1 - zero_cnt, targ2 - one_cnt)
            
            memo[(i,targ1,targ2)] = max(skip,include)
            return max(skip, include)

        return dfs(0, m , n)