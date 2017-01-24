#3.2
#How would you design a stack which, in addition to push and pop, 
#also has a function min which returns the minimum element? Push, 
#pop and min should all operate in O(!) time

#keep track of two stacks. stack 1 is the stack of all elements
#you push and pop. stack 2 is your "min stack" that keeps track
#of the most recently pushed minimum. 
#for example, you want to push the following numbers:
#3, 4, 2, 6, 0, 7
#stack 1: 3                     stack 2: 3
#stack 1: 3, 4                  stack 2: 3 (4 is not pushed, 4 > 3)
#stack 1: 3, 4, 2               stack 2: 3, 2 (2 is pushed, 2 < 3)
#stack 1: 3, 4, 2, 6            stack 2: 3, 2 (6 not pushed, 6 > 2)
#stack 1: 3, 4, 2, 6, 0         stack 2: 3, 2, 0 (0 is pushed, 0 < 2)
#stack 1: 3, 4, 2, 6, 7         stack 2: 3, 2, 0 (7 not pushed, 7 > 0)
#when popping an element from stack 1, you must check to see if it
# is also in stack 2 with the peek() function. if it is, pop the
#element from stack 2 as well. 
#the top element on stack 2 is always current minimum of the stack. 


