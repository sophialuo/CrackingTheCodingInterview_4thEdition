#8.5
#Implement an algorithm to print all valid (e.g. properly opened and closed) combination
#of n-pairs of parentheses
#EXAMPLE:
#input: 3 (e.g. 3 pairs of parentheses)
#output: ()()(), ()(()), ((())), (())()
def parentheses(num):
    return parentheses_helper(1, 0, num, '(')
    
def parentheses_helper(num_open, num_closed, total, seq):
    if num_closed == total and num_open == total:
        return seq 
    if num_open == total:
        return parentheses_helper(num_open, num_closed+1, total, seq+')') + ' '
    if num_closed == num_open:
        return parentheses_helper(num_open+1, num_closed, total, seq+'(') + ' '
    return parentheses_helper(num_open+1, num_closed, total, seq+'(') + ' ' + \
            parentheses_helper(num_open, num_closed+1, total, seq+')')
        
