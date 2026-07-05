class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            nextPerms = []
            for p in perms:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i, num)
                    nextPerms.append(pCopy)
            perms = nextPerms
        return perms