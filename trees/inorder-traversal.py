# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        q=[]
        levels=[]
        q.append(root)
        if root==None:
            return []
        while len(q)>0:
            temp_q=[]
            level=[]
            while len(q)>0:
                topNode = q.pop(0)
                if topNode!=None:
                    level.append(topNode.val)
                    if topNode.left!=None:
                        temp_q.append(topNode.left)
                    if topNode.right!=None:
                        temp_q.append(topNode.right)
            levels.append(level)
            q=temp_q
        return levels
