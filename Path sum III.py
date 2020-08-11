# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if root is None:
            return 0
        def dfs(node,summ,start):
            if summ==target:
                ans[0]+=1
            if node is None:
                return
            
            if start:
                dfs(node.left,node.val+summ,True)
                dfs(node.right,node.val+summ,True)
            else:
                dfs(node.left,float('inf'),False)
                dfs(node.left,node.val,True)
                dfs(node.right,float('inf'),False)
                dfs(node.right,node.val,True)
        ans=[0]
        dfs(root,float('inf'),False)
        return ans[0]//2
                
