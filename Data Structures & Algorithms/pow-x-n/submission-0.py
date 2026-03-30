class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = 1
        m = -n if n<0 else n
        for _ in range(m):
            y = x*y
        return y if n >= 0 else 1/y