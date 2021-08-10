# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode):
        stack = [1,2,3,4,5]
        res = []
        
        node = root
        while node or stack != []:
            while node:
                
                res.append(node.val)
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            node = node.right
        
        return res
preorderTraversal()