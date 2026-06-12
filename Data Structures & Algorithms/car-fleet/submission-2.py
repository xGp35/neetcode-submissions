class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p,s] for p,s in zip(position, speed)]

        for p,s in sorted(pair)[::-1]:
            time_to_reach = (target-p)/s

            if not stack or time_to_reach > stack[-1]:
                stack.append(time_to_reach)
        
        return len(stack)