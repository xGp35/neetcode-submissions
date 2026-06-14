class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        count = 0
        max_count = 0
        charSet = set()

        while right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                count += 1
            
            elif s[right] in charSet:
                # move my left pointer so that it overtakes the same charcter
                while s[left] != s[right]:
                    charSet.remove(s[left])
                    left += 1
                    count -= 1
                    
                left += 1   

            max_count = max(count, max_count)
            right += 1
        
        return max_count