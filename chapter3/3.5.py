#3.5
#Implement a MyQueue class which implements a queue using two stacks
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


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
    
    def enqueue(self, item):
        stack2 = Stack()
        #empty stack1 into stack2 
        while not self.stack1.isEmpty():
            elem = self.stack1.pop()
            stack2.push(elem)
       #push the element to stack1 so that it is at the bottom
        self.stack1.push(item)
        #push all of stack2 back into stack1
        while not stack2.isEmpty():
            elem = stack2.pop()  
            self.stack1.push(elem)
                  
    def dequeue(self, item):
        return self.stack1.pop()

