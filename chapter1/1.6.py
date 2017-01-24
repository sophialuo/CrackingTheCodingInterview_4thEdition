'''
1.6
Given an image represented by a NXN matrix
where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 
degrees. Can you do this in place?
'''
import math

def rotate(matrix):
    N = len(matrix)
    ans = [[0 for r in range(N)] for c in range(N)]
    for r in range(N):
        for c in range(N):
            ans[c][N-r-1] = matrix[r][c]
    return ans

def rotate_inplace(matrix):
    n = len(matrix)
    outer = math.floor(n/2)-1
    inner = math.ceil(n/2)-1
    for i in range(outer):
        for j in range(inner):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n-i-1]
            matrix[j][n-i-1] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[n-j-1][i]
            matrix[n-j-1][i] = temp


    