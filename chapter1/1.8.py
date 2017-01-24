'''
1.8
Assume you have a method isSubstring which
checks if one word is a substring of another.
given two strings, s1 and s2, write code to 
check if s2 is a rotation of s1 using only 
one call to isSubstring
'''
def is_substring(orig_string, try_string):
    try:
        orig_string.index(try_string)
        return True
    except ValueError:
        return False

def is_rotation(orig_string, try_string):
    if len(orig_string) != len(try_string):
        return False
    
    for i in range(1,len(try_string)):
        substr_head = try_string[0:i]
        substr_tail = try_string[i:]
        if is_substring(orig_string, substr_head) and \
        is_substring(orig_string, substr_tail):
            return True
    return False