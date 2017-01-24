#8.2
#Imagine a robot sitting on the upper left hand
#corner of an NXN grid. The robot can only move 
#in two directions: right and down. How many 
#possible paths are there for the robot?

#(n-1)*(n-1) possible paths. 
#each path has n-1 steps to the right and n-1
#steps down, which totals to 2n-2 total steps. 
#out of the 2n-2 steps, the robot always moves 
#down n-1 times, so we there are 2n-2 choose n-1
#possible paths: (2n-2)!/((n-1)! * (n-1)!)

#8.2 follow up
#Imagine certain squares are off limits, such
#that the robot can't step on them. Design
#an algorithm to get all possible paths for 
#the robot

#implement a DFS that stores visited grid spaces.
#upon reaching the target grid space, print the
#visited grid spaces
    
