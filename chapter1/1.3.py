'''
1.3
Design an algorithm and write code to remove the
duplicate characters in a string without using any
additional buffer. Note: one or two additional 
variables are fine. 
'''
def remove_duplicates(word):
    ans = ''
    ascii_table = [False for x in range(128)]    
    for c in word:
        num = ord(c)
        if not ascii_table[num]:
            ans += c
            ascii_table[num] = True
    return ans
