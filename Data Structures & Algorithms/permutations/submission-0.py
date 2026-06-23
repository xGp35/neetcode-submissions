class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            resPerms = []
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, n)
                    resPerms.append(pCopy)
            perms = resPerms
        return perms