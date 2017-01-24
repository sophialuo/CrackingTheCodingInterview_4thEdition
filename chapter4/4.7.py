#4.7 
#You have two very large binary trees: T1, with
#millions of nodes, and T2, with hundreds of nodes.
#Create an algorithm do decide if T2 is a subtree of T1
        
#do an inorder traversal of T1 (inorder1) and an inorder
#traversal of T2 (inorder2). also do a preorder traversal
#of T1 (preorder1) and a preorder traversal of T2 
#preorder2). if preorder2 is a substring of preorder1
#and inorder2 is a substring of inorder1, then T2 is a 
#subtree of T1