# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        """
        core principle is same as max depth, jsut keep adding value at each level and check         if it is leaf node
        if it is leaf node, return currentValue == sum and at end of call stack, check for           one occurrence of True
        """
        if root==None:
            return False
        return self.checkPath(root,root.val,sum)
    def checkPath(self,root,val,s):
        
        if root and root.left==None and root.right==None:
            return val==s
        else:
            if root and root.left and self.checkPath(root.left, val+root.left.val , s):
                    return True
            if root and root.right and self.checkPath(root.right,val+root.right.val,s):
                    return True
        return False
                
