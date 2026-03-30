class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #If target is even, handle target/2 initially:
        index_set = []
        if target%2 ==0:
            tby2 = target/2
            for i,elem in enumerate(nums):
                if elem == tby2:
                    index_set.append(i)
            if len(index_set) > 1:
                return index_set
        
        # Create complementary Set
        compl_set = set()
        for elem in nums:
            compl_set.add(target-elem)
        
        idx1, idx2 = -1, -1
        #Find idx1
        for i, elem in enumerate(nums):
            if elem in compl_set and elem != target/2:
                idx1 = i
                break

        #Find idx2
        for j,elem2 in enumerate(nums):
            if j == idx1:
                continue
            if elem2 == target - nums[idx1]:
                idx2 = j
        
        return [idx1, idx2]
            