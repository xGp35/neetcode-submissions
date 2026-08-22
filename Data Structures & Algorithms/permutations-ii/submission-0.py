class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        resPerms = [[]]
        for n in nums:
            temp = []
            for p in resPerms:
                for i in range(len(p)+1):

                    if i > 0 and p[i-1] == n:
                        break # if my previous character is same, I can break.
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    temp.append(pCopy)
            resPerms = temp
        
        return resPerms