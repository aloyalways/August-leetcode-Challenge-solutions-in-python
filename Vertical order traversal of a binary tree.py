from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        verticalT=defaultdict(list)
        def helper(node,x,y):
            if node is None:
                return
            helper(node.left,x-1,y+1)
            helper(node.right,x+1,y+1)
            verticalT[(x,y)].append(node.val)
        
        helper(root,0,0)
        output=[]
        prev=float('inf')
        for k,v in sorted(verticalT.items()):
            if k[0]!=prev:
                output.append([])
            output[-1]+=sorted(v)
            prev=k[0]
        return output
            
