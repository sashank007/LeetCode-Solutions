# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder)==0:
            return None
        if len(postorder)>0:
            currentRootVal = postorder[-1]
            root = TreeNode(currentRootVal)
            index_of_root_at_inorder = inorder.index(currentRootVal)
            length_of_left_subtree=len(inorder[:index_of_root_at_inorder])
            root.left = self.buildTree(inorder[:index_of_root_at_inorder] , postorder[:length_of_left_subtree])
            root.right=self.buildTree(inorder[index_of_root_at_inorder+1:] ,  postorder[length_of_left_subtree:-1])
            return root
