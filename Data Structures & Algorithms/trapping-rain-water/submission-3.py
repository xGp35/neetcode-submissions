class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix_arr = [0]*n
        prefix = 0
        for i in range(n):
            # largest height to the left of height[i]
            prefix_arr[i] = prefix
            prefix = max(height[i], prefix)
        
        suffix_arr = [0]*n
        suffix = 0
        for i in range(n-1, -1, -1):
            # largest height to the right of height[i]
            suffix_arr[i] = suffix
            suffix = max(height[i], suffix)
        
        water = [0]*n
        for i in range(n):
            water[i] = min(prefix_arr[i], suffix_arr[i]) - height[i]
        
        water_new = [0 if val < 0 else val for val in water]
        return sum(water_new)