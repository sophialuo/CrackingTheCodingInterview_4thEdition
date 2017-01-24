#10.2
#There are three ants on different vertices of a 
#triangle. what is the probability of collision 
#between any two or all of them) if they start 
#walking on the sides of the triangle?
#Similarly, find the probability of collision with
#'n' ants on an 'n' vetex polygon


#each ant can walk in two different reactions so the
#total number of ways the ants can move is 2^3. 
#the only two ways that the ants will ont collide
#is if they all walk clockwise or counterclockwise.
#P(collision): (2^3-2)/(2^3)
#generalization to n ants on n vertices
#P(collision): (2^n-2)/(2^n)

