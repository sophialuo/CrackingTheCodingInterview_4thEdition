
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
        
#4.1
#Implement a function to check if a tree is balanced. 
#For the purpose of this question, a balanced tree is 
#defined to be a tree such that no two leaf nodes 
#differ in distance from the root by more than one
def is_balanced(tree):
    left_height = find_height(tree.leftChild)
    right_height = find_height(tree.rightChild)
    if abs(left_height-right_height) <= 1:
        return True
    return False

def find_height(subtree):
    if not subtree:
        return 0
    return 1 + max(find_height(subtree.leftChild), find_height(subtree.rightChild))

