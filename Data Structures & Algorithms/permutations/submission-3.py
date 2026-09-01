class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(i):
            if i == len(nums): return [[]]

            temp = []
            perms = dfs(i+1)
            for p in perms:
                for j in range(0, len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    temp.append(pCopy)
            return temp
        
        return dfs(0)

