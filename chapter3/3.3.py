#3.3
#Imagine a (literal) stack of plates. If the stack gets too high, it
#might topple. Therefore, in real life, we would likely start a new 
#stack when the previous stack exceeds some threshold. Implement a 
#data structure SetOFStacks that mimics this. SetOFStacks should be 
#composed of several stacks, and should create a new stack once the
#previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
#should behave identically to a single stack (that is, pop() should 
#return the same values as it would if there was just a single stack)

#3.3 followup.
#Implement a function popAt(int index) which performs a pop operation on 
#a specific sub-stack 

class SetOfStacks:
    def __init__(self, c):
        self.stacks = []
        self.capacity = c
    
    def push(self, num):
        last_index = len(self.stacks)-1
        last_stack = self.stacks[last_index]
        if len(last_stack) < self.capacity:
            self.stacks[last_index].append(num)
        else:
            self.stacks.append([num,])
    
    def pop(self):
        return self.stacks[len(self.stacks)-1].pop()
    
    def popAt(self, index):
        return self.stacks[index].pop()
        
