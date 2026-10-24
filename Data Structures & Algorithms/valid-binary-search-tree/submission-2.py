# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(node,minlimit,maxlimit):
            if not node:
                return 
            if node.val<=minlimit or node.val>=maxlimit:
                return -1
            left = bst(node.left,minlimit,min(node.val,maxlimit))
            right = bst(node.right,max(node.val,minlimit),maxlimit)
            if left==-1 or right==-1:
                return -1
        result = bst(root,float('-inf'),float('inf'))
        if result == -1:
            return False
        return True
        