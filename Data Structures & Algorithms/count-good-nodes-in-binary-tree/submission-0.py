# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def checkgood(node,maxlimit):
            if not node:
                return 
            nonlocal count
            if node.val >= maxlimit:
                count +=1
                maxlimit = node.val
            checkgood(node.left,maxlimit)
            checkgood(node.right,maxlimit)

        checkgood(root,float('-inf'))
        return count
            
