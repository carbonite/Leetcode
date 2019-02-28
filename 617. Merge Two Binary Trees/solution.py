# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        node = None
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        elif not t1 and t2:
            node = t2
        elif not t2 and t1:
            node = t1
        
        return node
            