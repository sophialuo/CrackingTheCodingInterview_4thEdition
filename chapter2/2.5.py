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
    


#2.5
#Given a circular linked list, implement an algorithm 
#which returns node at the beginning of the loop.
#DEFINITION 
#Circular linked list: A (corrupt) linked list in 
#which a node’s next pointer points to an earlier node, 
#so as to make a loop in the linked list. 
#EXAMPLE 
#input: A -> B -> C -> D -> E -> C 
#[the same C as earlier] output: C
def find_cycle_beginning(head):
    pointer1 = head
    pointer2 = head.next_node.next_node
    #detect cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next_node
        pointer2 = pointer2.next_node.next_node
    #find beginning of cycle
    pointer1 = head
    while pointer1 != pointer2:
        pointer1 = pointer1.next_node
        pointer2 = pointer2.next_node.next_node
    
    return pointer2
    
#test case:
a = Node('A', None)
b = Node('B', None)
c = Node('C', None)
d = Node('D', None)
e = Node ('E', None)
a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
e.next_node = c
beginning = find_cycle_beginning(a)
print(beginning.data)