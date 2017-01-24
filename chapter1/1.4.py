'''
1.4
Write a method to decide if two strings are anagrams
or not
'''

#a short one-line method
def is_anagram_simple(word):
    return word == word[::-1]

#another way to accomplish the same task
def is_anagram(word):
    length = len(word)
    #if length or word is even
    first = ''
    second = ''
    if length%2 == 0:
        first = word[:int(length/2)]
        second = word[int(length/2):]
    #elif length of word is odd
    elif length%2 == 1:
        first = word[:int(length/2)]
        second = word[int(length/2)+1:]

    for i in range(len(first)):
        if first[i] != second[len(second)-i-1]:
                return False
    return True
