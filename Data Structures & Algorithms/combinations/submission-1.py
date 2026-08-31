class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def helper(i, currComb):
            if len(currComb) >= k:
                combs.append(currComb.copy())
                return
            
            for j in range(i, n+1):
                currComb.append(j)
                helper(j+1, currComb)
                currComb.pop()

        helper(1, [])
        return combs

        