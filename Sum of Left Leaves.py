# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.ans=0
        def summ(node,side):
            if node is None:
                return True
            mtL=summ(node.left,'left')
            mtR=summ(node.right,'right')
            if mtL and mtR and side=='left':
                self.ans+=node.val
        summ(root,'root')
        return self.ans
            
