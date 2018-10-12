# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import copy
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        node = head
        while node is not None:
            if node.next and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
                
