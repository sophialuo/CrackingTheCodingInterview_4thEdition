#3.6
#Write a program to sort a stack in ascending order. You should not 
#make any assumptions about how the stack is implemented. The 
#following are the only functions that should be used to write 
#this program: push | pop | peek | isEmpty

#essentially: push elem x from stack 1 into stack 2 if top elem of stack 2 is 
#smaller. otherwise, push elements from stack 2 to stack 1 until find a 
#number that is less than x or until stack 2 is empty. then push x to stack 2.

class Stack:
     def __init__(self):
         self.items = []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         #removes most recent element added (last element of list)
         return self.items.pop()
         
     def isEmpty(self):
         return self.items == []
         
def sort_stack(orig):
    ans = Stack()
    while not orig.isEmpty():
        temp = orig.pop()
        if ans.isEmpty() or temp > ans.peek():
            ans.push(temp)
        else:
            #push elements from ans to orig until number less than temp
            while ans.peek() > temp:
                orig.push(ans.pop())
                if ans.isEmpty():
                    break
            ans.push(temp)
    return ans
