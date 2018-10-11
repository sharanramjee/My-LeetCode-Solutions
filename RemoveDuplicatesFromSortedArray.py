class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        num_list = list(num_set)
        num_list.sort()
        nums[:] = num_list[:]
        return len(nums)
        
