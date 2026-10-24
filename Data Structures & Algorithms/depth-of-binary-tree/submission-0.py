# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftlen = 0
        rightlen = 0
        if root.left:
            leftlen = self.maxDepth(root.left)
        if root.right:
            rightlen = self.maxDepth(root.right)
        return max(leftlen,rightlen)+1
        