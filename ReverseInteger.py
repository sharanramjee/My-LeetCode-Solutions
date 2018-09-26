class Solution(object):
    def count_zeros(self, int_list):
        count = 0
        for digit in int_list:
            if digit == '0':
                count += 1
            else:
                break
        return count
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        int_string = str(x)
        int_list = list(int_string)
        if int_list[0] != '-':
            int_list.reverse()
            count = self.count_zeros(int_list)
            reversed_int = int(''.join(int_list[count:]))
        else:
            int_list = int_list[1:]
            int_list.reverse()
            count = self.count_zeros(int_list)
            reversed_int = int(''.join(list('-') + int_list[count:]))
        if reversed_int < (-2**31) or reversed_int > ((2**31)-1):
            return 0
        else:
            return reversed_int
