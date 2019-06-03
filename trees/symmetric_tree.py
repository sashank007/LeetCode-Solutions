# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        to check for symmetric tree, we first need to satisfy two           conditions recursively for each left and right subtree:
        condition 1: leftSubtre.left==rightSubtree.right
        condition 2: leftSubtree.right==rightSubtree.left"""
        return root==None or self.checkSymmetric(root.left,root.right)
    def checkSymmetric(self,leftNode,rightNode):
        if leftNode==None and rightNode==None:
            return True
        elif leftNode!=None and rightNode!=None:
            return leftNode.val==rightNode.val and self.checkSymmetric(leftNode.left , rightNode.right) and self.checkSymmetric(leftNode.right , rightNode.left)
        return False
