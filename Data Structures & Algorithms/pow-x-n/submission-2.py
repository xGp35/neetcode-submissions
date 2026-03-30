class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper (x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x*x, abs(n//2))

            return x*res if n%2 else res

        return helper(x, abs(n)) if n >=0 else 1/helper(x, abs(n))
