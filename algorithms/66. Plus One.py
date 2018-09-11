#carry all the time

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits or len(digits) == 0:
            return []
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            cur = digits[i] + carry
            carry = cur // 10
            digits[i] = cur % 10
        if carry:
            digits.insert(0,1)
        return digits
