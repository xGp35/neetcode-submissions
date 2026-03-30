class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0]*n
        prefix_max[0] = height[0]
        for i in range(1, n):
            prefix_max[i] = max(height[i], prefix_max[i-1])
        print(prefix_max)

        suffix_max = [0]*n
        suffix_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(height[i], suffix_max[i+1])
        print(suffix_max)
        
        # Calculate amount of water trapped at position i.
        water = [0]*n
        for i in range(n):
            # height[l] = tallest bar to the left = prefix_max[i]
            # height[r] = tallest bar to the right = suffix_max[i]  
            water[i] = min(prefix_max[i], suffix_max[i]) - height[i]

        # max_water = 0
        # curr_water = 0
        # idx = 0
        # while (idx < n):
        #     max_water = max(curr_water, max_water)
        #     #print(f"max water when idx is {idx}  = {max_water}")
        #     if water[idx] == 0:        
        #         curr_water = 0
        #     elif water[idx] != 0:
        #         curr_water = curr_water + water[idx]
        #     idx += 1
        # return max_water
        return(sum(water))
