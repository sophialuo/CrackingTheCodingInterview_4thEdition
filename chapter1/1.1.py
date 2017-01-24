'''
1.1
Implement an algorithm to determne if a string has
all unique characters. 
'''

def unique_chars(word):
    char_count = {}
    for c in word:
        if c in char_count:
            return False
        char_count[c] = 1
    return True

#a more efficient algorithm
def unique_chars_better(word):
    ascii_table = [False for x in range(128)]
    for c in word:
        num = ord(c)
        if ascii_table[num]:
            return False
        ascii_table[num] = True
    return True