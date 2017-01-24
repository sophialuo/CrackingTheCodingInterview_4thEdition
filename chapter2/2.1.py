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
    
#2.1 
#Write code to remove duplicates from an unsorted list
#follow up: how would you solve this without a temporary
#buffer
def remove_duplicates(head):
    counts = {}
    counts[head.data] = 1
    prev = head
    cur = head.next_node
    while cur:
        data = cur.data
        if data in counts:
            prev.next_node = cur.next_node
            cur = prev.next_node
        else:
            counts[data] = 1
            prev = cur
            cur = cur.next_node
    return head


