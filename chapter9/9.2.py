#9.2
#Write a method to sort an array of strings so that
#the anagrams are next to each other
def sort_anagrams(lst):
    ans = {}
    for i in range(len(lst)):
        word = lst[i]
        ascii_table = [0 for i in range(127)]
        for char in word:
            val = ord(char)
            ascii_table[val] += 1
        ascii_table = tuple(ascii_table)
        if ascii_table in ans:
            ans[ascii_table].append(word)
        else:
            ans[ascii_table] = [word,]
    ans_lst = []
    for key in ans:
        ans_lst.extend(ans[key])
    return ans_lst
    
    
