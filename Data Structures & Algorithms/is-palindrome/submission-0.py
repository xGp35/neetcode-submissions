class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left_ptr = 0
        right_ptr = len(s)-1
        while(left_ptr<right_ptr):
            left = s[left_ptr]
            right = s[right_ptr]
            if not left.isalnum():
                left_ptr += 1
            elif not right.isalnum():
                right_ptr -= 1
            elif left != right:
                return False
            else:
                left_ptr += 1
                right_ptr -= 1
        return True      