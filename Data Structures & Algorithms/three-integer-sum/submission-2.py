class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # As the elements are sorted and we are scanning only next elements 
            # for each nums[i], once we read postive num[i], we can break 
            # as we are sure the next elements won't sum up to 0. 
            if nums[i] > 0:
                break
            
            #Skipping duplicate in outer loop
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            lp = i+1
            rp = len(nums) - 1

            while(lp < rp):
                total = nums[i] + nums[lp] + nums[rp]

                if total == 0:
                    res.append([nums[i], nums[lp], nums[rp]])
                    
                    lp += 1
                    rp -= 1

                    # Skipping duplicate elements in inner loop
                    while(lp < rp and nums[lp] == nums[lp-1]):
                        lp +=1
                    while(lp < rp and nums[rp] == nums[rp+1]):
                        rp -=1
                
                elif total < 0:
                    lp += 1
                elif total >0:
                    rp -= 1
            
        return res
                     

        



















