
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


        

#4.4 
#Given a binary search tree, design an algorithm 
#which creates a linked list of all the ndoes at 
#each depth (ie. if you have a tree with depth 
#D, you'll have D linked lists)
def depth_nodes(tree):
    #put the nodes in order by level; top to bottom
    order = []
    queue = [tree]
    while queue != []:
        cur_element = queue.pop(0)
        order.append(cur_element.key)
        if cur_element.leftChild:
            queue.append(cur_element.leftChild)
        if cur_element.rightChild:
            queue.append(cur_element.rightChild)
    #make linked lists out of levels 1 through D-1
    ans = []
    index = 0
    multiplier = 1
    while index + multiplier < len(order):
        head = Node(order[index], None)
        cur = head
        for i in range(1,multiplier):
            node = Node(order[i+index], None)
            cur.next = node
            cur = cur.next
        ans.append(head)
        index += multiplier
        multiplier = multiplier * 2
    #add level D (the remaining leaves)
    head = Node(order[index], None)
    cur = head
    index += 1
    while index < len(order):
        node = Node(order[index], None)        
        cur.next = node
        cur = cur.next
        index += 1
    ans.append(head)
    #return result
    return ans

#from exercise 4.3 -- using this method to create a test case
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
ans = depth_nodes(tree)
for i in range(len(ans)):
    head = ans[i]
    print(head.data, end = ' ')
    cur = head.next
    while cur:
        print(cur.data, end = ' ')
        cur = cur.next
    print('')
    

