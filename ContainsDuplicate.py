class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        list_len = len(nums)
        set_len = len(set(nums))
        if set_len == list_len:
            return False
        else:
            return True
