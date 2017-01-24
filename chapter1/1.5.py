'''
1.5
write a method to replace all spacecs in 
in a string with '%20'
'''

def replace_spaces(words):
    ans = ''
    for c in words:
        if c == ' ':
            ans += '%20'
        else:
            ans += c
    return ans