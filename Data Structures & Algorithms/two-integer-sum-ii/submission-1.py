class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers)-1
        idx1 = 0
        idx2 = 0
        while(lp < rp):
            if numbers[lp] + numbers[rp] == target:
                idx1, idx2 = lp, rp
                break
            elif numbers[lp] + numbers[rp] < target:
                lp += 1
            elif numbers[lp] + numbers[rp] > target:
                rp -= 1
        return [idx1+1, idx2+1]