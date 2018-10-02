class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_str = [str(digit) for digit in digits]
        num_str = ''.join(digit_str)
        num = int(num_str)
        num += 1
        num_str = str(num)
        digits = [int(digit) for digit in num_str]
        return digits
