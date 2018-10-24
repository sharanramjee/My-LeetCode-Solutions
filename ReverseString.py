class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = list(s)
        str_list.reverse()
        return ''.join(str_list)
