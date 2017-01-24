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



#for testing purposes
def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.leftChild)
        preorder(tree.rightChild)
        

#4.6
#Design an algorithm and write code to find the 
#first common ancestor of two nodes in a binary tree. 
#Avoid storing additional nodes in a data structure
#NOTE: This is not necessarily a binary search tree
def common_ancestor(node1, node2):
    #find paths of nodes for node1
    ancestry1 = []
    cur = node1
    while cur:
        ancestry1.append(cur)
        cur = cur.parent
    #check if any node in path of nodes for node2 
    #in order of lowest potential common ancestor
    #to highest
    cur = node2
    while cur:
        for i in range(len(ancestry1)):
            if cur == ancestry1[i]:
                return cur
        cur = cur.parent
    return ancestry1[len(ancestry1)-1] #root of tree
        
