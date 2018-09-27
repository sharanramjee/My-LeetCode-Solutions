class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_list = list()
        num_list = list()
        for num in nums:
            if num != 0:
                num_list.append(num)
            else:
                zero_list.append(num)
        number_list = num_list + zero_list
        for index in range(len(number_list)):
            nums[index] = number_list[index]
