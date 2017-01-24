#8.4
#Write a method to compute all permutations of a string
def perm(string):
    if len(string) <= 1:
        return [string]
    first_char = string[0]
    perms = perm(string[1:])
    ans = []
    for p in perms:
        for i in range(len(p)+1):
            ans.append(p[:i]+first_char+p[i:]) #insert the character everywhere
    return ans

