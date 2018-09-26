# Maximum Depth of Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recurse(self, node):
        if node == None:
            return 0
        leftDepth = self.recurse(node.left)
        rightDepth = self.recurse(node.right)
        if leftDepth > rightDepth:
            return leftDepth + 1
        return rightDepth + 1
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            max_depth = self.recurse(root)
            return max_depth
