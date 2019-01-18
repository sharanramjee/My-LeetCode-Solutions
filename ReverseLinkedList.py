# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        new_tail = None
        while(node != None):
            new_node = node.next
            node.next = new_tail
            new_tail = node
            node = new_node
        return new_tail
            
        
