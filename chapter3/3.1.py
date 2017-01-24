#3.1
#Describe how you can use a single array to implement three stacks


#stack 1 starts at 0 and pushes in the positive direction, stack 2 
#starts at n/3 and pushes in the positive direction, and stack 3
#starts at n-1 and pushes in the negative direction. every time you
#push an element into stack 1 or 2, increment that stack's index. every
#time you pop an element from stack 1 or 2, decrement that stack's index.
#it is the opposite for stack 3 where pushing means decrementing the
#index and popping involves incrementing the index. if the middle stack
#ever crashes into another stack, shift the entire stack in the direction
#away from the collision and update the index accordingly. for instance,
#if pushing an element to stack 1 collides with the first element of 
#stack 2, shift stack 2 to the positive direction by x elements and add
#x to the stack's index. 


