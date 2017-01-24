#9.1
#You are given two sorted arrays, A and B, and A
#has a large enough buffer at the end to hold B. 
#Write a ethod to merge B into A in sorted order
def merge(A, B):
    ans = []
    indexA = 0
    indexB = 0
    while indexB < len(B):
        if A[indexA] < B[indexB]:
            ans.append(A[indexA])
            indexA += 1
        else:
            ans.append(B[indexB])
            indexB += 1
    if indexA < len(A):
        ans.extend(A[indexA:])
    return ans

