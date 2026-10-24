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
                return True
            if node.val<=minlimit or node.val>=maxlimit:
                return False
            return bst(node.left,minlimit,node.val) and bst(node.right,node.val,maxlimit)
        return bst(root,float('-inf'),float('inf'))