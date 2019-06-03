# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """
        The concept remains that first value in preorder is root node, so we pop it and create left and right subtrees          based on the root node"""
        if not preorder and not inorder:
            return None
        if preorder and inorder:
            currentRootVal = preorder.pop(0)
            root = TreeNode(currentRootVal)
            get_index_inorder = inorder.index(currentRootVal)
            length= len(inorder[:get_index_inorder])

            root.left= self.buildTree( preorder,inorder[:get_index_inorder] )
            root.right = self.buildTree(preorder,inorder[get_index_inorder+1:])
            return root
        else:
            return None
