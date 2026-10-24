# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def judge(node):
            if not node:
                return 0
            leftlen = judge(node.left)
            rightlen = judge(node.right)
            if leftlen == -1 or rightlen == -1 or abs(leftlen-rightlen)>1:
                return -1
            return max(leftlen,rightlen)+1

        res = judge(root)
        if res == -1:
            return False
        return True
