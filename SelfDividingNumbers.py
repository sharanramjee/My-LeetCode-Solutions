class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_divide_list = list()
        for number in range(left, right+1):
            digit_list = [int(digit) for digit in list(str(number))]
            if 0 in digit_list:
                continue
            divisible = False
            for digit in digit_list:
                if number % digit != 0:
                    divisible = True
            if divisible is False:
                self_divide_list.append(number)
        return self_divide_list
            
                
