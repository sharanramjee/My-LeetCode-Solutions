# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        if k == 0:
            return head
        list_linked = list()
        temp_head = head
        while temp_head is not None:
            list_linked.append(temp_head.val)
            temp_head = temp_head.next
        k %= len(list_linked)
        if k == 0:
            return head
        for index in range(k):
            list_linked[:] = list_linked[-1:] + list_linked[:-1]
        temp_head = head
        for value in list_linked:
            temp_head.val = value
            temp_head = temp_head.next
        return head
