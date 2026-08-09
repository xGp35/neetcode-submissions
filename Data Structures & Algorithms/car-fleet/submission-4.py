class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = list(zip(position,speed))
        pos_spd.sort(key = lambda x: x[0])

        time = []
        for pos, spd in pos_spd:
            time.append((target - pos) / spd)

        result = []
        nums= time
        stack = []
        for i, x in enumerate(nums):
            while stack and x >= nums[stack[-1]]:
                j = stack.pop()
                # x is the next greater element of nums[j]
                # do something with it
            stack.append(i)
        
        return len(stack)