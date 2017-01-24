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
    

#2.4
#You have two numbers represented by a linked list, where
#each node contains a single digit. The digits are stored 
#in reverse order, such that the 1's digit is at the head 
#of the list. Write a function that adds the two numbers 
#and returns the sum as a linked list
#EXAMPLE
#input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
#output: 8 -> 0 -> 8
def add(head1, head2):
    cur_sum = head1.data + head2.data
    leftover = 0
    if cur_sum >= 10:
        leftover = 1
        cur_sum -= 10
    head_ans = Node(cur_sum, None)
    cur_ans = head_ans
    
    cur1 = head1.next_node
    cur2 = head2.next_node
    while cur1 and cur2:
        cur_sum = cur1.data + cur2.data + leftover
        leftover = 0
        if cur_sum >= 10:
            leftover = 1
            cur_sum -= 10  
        cur_ans.next_node = Node(cur_sum, None)
        cur_ans = cur_ans.next_node
        cur1 = cur1.next_node
        cur2 = cur2.next_node
    return head_ans 
    
