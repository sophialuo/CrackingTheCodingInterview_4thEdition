
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
        

#4.3
#Given a sorted (increasing order) array, write an 
#algorithm to create a binary tree with minimal height
def array_to_tree(array):
    mid_index = int(len(array)/2)
    mid_val = array[mid_index]
    node = TreeNode(mid_val, None, None, None)
    return array_to_tree_helper(node, array[:mid_index], array[mid_index+1:])
    
    
def array_to_tree_helper(node, arr_left, arr_right):
    if arr_left == [] and arr_right == []:
        return node
    elif arr_left == []: #no more possible left children
        right_val = arr_right[0]
        right_node = TreeNode(right_val, None, None, parent = node)
        node.rightChild = right_node
        return node #no more possible right children
    elif arr_right == []:
        left_val = arr_left[0]
        left_node = TreeNode(left_val, None, None, parent = node)
        node.leftChild = left_node
        return node
    #create left node
    left_index = int(len(arr_left)/2)
    left_val = arr_left[left_index]
    left_node = TreeNode(left_val, None, None, parent = node)
    #create right node
    right_index = int(len(arr_right)/2)
    right_val = arr_right[right_index]
    right_node = TreeNode(right_val, None, None, parent = node)
    #set children of node
    node.leftChild = left_node
    node.rightChild = right_node
    #recursion
    array_to_tree_helper(left_node, arr_left[:left_index], arr_left[left_index+1:])
    array_to_tree_helper(right_node, arr_right[:right_index], arr_right[right_index+1:])
    #what to return?
    return node
    
#test case    
array = [1,2,3,4,5,6,7,8,9,10]
tree = array_to_tree(array)
preorder(tree) #see if algorithm is correct

