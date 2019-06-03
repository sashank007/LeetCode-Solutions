"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        """
        have two directions to go in , horizontal and vertical, there are two conditions that need to be satisfied:
        condition 1: if that level's parent node has a left node, then it must point to that parent's right node
        condition 2: if that level's parent node, has a next node , then the parent's right node must point to              parent.next.left"""
        verticalNode = root
        while verticalNode:
            horizontalNode=verticalNode
            while horizontalNode:
                if horizontalNode.left!=None:
                    horizontalNode.left.next=horizontalNode.right
                if horizontalNode.right!=None and horizontalNode.next!=None:
                    horizontalNode.right.next=horizontalNode.next.left
                horizontalNode=horizontalNode.next
            verticalNode=verticalNode.left
        return root
