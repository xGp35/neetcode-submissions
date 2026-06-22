class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def helper(i, currComb, combs, n, k):
            if len(currComb) >= k:
                combs.append(currComb.copy())
                return
            
            for j in range(i, n+1):
                currComb.append(j)
                helper(j+1, currComb, combs, n, k)
                currComb.pop()

        helper(1, [], combs, n, k)
        return combs

        