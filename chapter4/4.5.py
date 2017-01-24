# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:39:00 2017

@author: 16sophial
"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class TreeNode:
   def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent


        
#4.5
#Write an algorithm to find the 'next' node (i.e.,
#in-order successor) of a given node in a binary
#search tree where each node has a link to its parent
def inOrderSuccessor(treenode):
    #if a right child of treenode exists, find the leftmost child
    #of that rightchild
    if treenode.right:
        current = treenode.right
        while current:
            if not current.left:
                break
            current = current.left
        return current
    #if a right cihld of the treenode doesn't exist, traverse upward
    #until you see a node which is the left child of its parent. that
    #parent is the successor
    p = treenode.parent
    while p and (treenode == p.right):
        treenode = p 
        p = p.parent
    return p


