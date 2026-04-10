class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            temp = carry + digits[i]
            digits[i] = (temp)%10
            carry = temp // 10
            if carry == 0:
                break
        
        if carry == 1:
            digits = [1] + digits
        return digits


