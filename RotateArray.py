class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if k > len(nums):
            k %= len(nums)
        temp_1 = nums[-k:]
        temp_2 = nums[:len(nums)-k]
        temp_list = temp_1 + temp_2
        for index in range(len(nums)):
            nums[index] = temp_list[index]
                
