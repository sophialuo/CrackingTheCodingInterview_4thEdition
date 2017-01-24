'''
1.2
Write code to reverse a C-Style String. C-String means
that "abcd" is represented as five characters, 
including the null character. 
'''
def reverse_string(word):
    ans = ''
    for i in range(len(word)-1, -1,-1):
        ans += word[i]
    return ans