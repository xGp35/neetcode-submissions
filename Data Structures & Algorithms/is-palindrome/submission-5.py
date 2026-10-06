class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [char.lower() for char in s if char.isalnum()]

        left, right = 0, len(new_s) -1

        while (left < right):
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1

        return True
        

        