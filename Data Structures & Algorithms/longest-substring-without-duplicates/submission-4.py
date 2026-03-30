class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0
        letters = set()
        # As r was initialized to 0, so letters is initialized to empty set.
        # Empty set initialization goes hand in hand with r being set to 0

        maxlen = 0
        
        while r < len(s):
            while s[r] in letters:
                # In the first iteration, this will not run because,
                # We are at r = 0 and set is empty so far, 
                # We have a clever place to add the addtion of chars
                # to our set called letters 
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            # The above is the clever placement I was talking about
            maxlen = max(maxlen, r-l+1)
            r+=1
        return maxlen

        
        