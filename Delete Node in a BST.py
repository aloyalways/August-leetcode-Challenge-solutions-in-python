# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        
        def minNode(node):
            curr=node
            while curr.left is not None:
                curr=curr.left
            return curr
        
        def delNode(node,key):
            if node is None:
                return node
            if key<node.val:
                node.left=delNode(node.left,key)
            elif key>node.val:
                node.right=delNode(node.right,key)
            else:
                if node.left is None:
                    temp=node.right
                    node=None
                    return temp
                elif node.right is None:
                    temp=node.left
                    node=None
                    return temp
                temp=minNode(node.right)
                node.val=temp.val
                node.right=delNode(node.right,temp.val)
            return node
        yo=delNode(root,key)
        return yo
