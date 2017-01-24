class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
        

            
#make a linked list given a list of nums where element 0 is the head
def make_testcase(numlist):
    #assume numlist is at least two elements wrong
    head = Node(numlist[0], None)
    cur = Node(numlist[1], None)
    head.next_node = cur
    for i in range(2, len(numlist)):
        new_node = Node(numlist[i], None)
        cur.next_node = new_node
        cur = new_node
    return head

#print out all data
def read_linkedlist(head):
    ans = str(head.data) + ' '
    cur = head.next_node
    while cur:
        ans += str(cur.data) + ' '
        cur = cur.next_node
    print(ans)
    


#2.2
#find an algorithm that returns the nth to last element of a 
#linked list
def nth_to_last(head, n):
    size = 1
    cur = head.next_node
    while cur:
        size += 1
        cur = cur.next_node
    
    cur = head
    for i in range(size-n):
        cur = cur.next_node
    return cur

#a smarter way to accomplish the same task 
def nth_to_last_smarter(head, n):
    pointer1 = head
    pointer2 = head
    for i in range(n-1):
        pointer2 = pointer2.next_node
    
    while pointer2.next_node:
        pointer1 = pointer1.next_node
        pointer2 = pointer2.next_node
    
    return pointer1
    
