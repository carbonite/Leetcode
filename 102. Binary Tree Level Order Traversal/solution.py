# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        sol = []
        rev = False
        
        if root:
            queue.append(root)
            
            while queue:
                newQueue = []
                levelSol = []
                
                # visit every node in current queue
                for node in queue:
                    # Add its value to solution and append its children for next level
                    levelSol.append(node.val)
                    if node.left:
                        newQueue.append(node.left)
                    if node.right:
                        newQueue.append(node.right)

                sol.append(levelSol)
                
                # update queue for next order
                queue = newQueue
                    
        return sol
