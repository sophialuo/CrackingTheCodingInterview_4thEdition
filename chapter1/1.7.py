'''
1.7 
Write an algorithm such that if an element
in an MXN matrix is 0, its entire row 
and column is set to 0
'''
def zeroes(matrix, M, N):
    rows_with_zeros = [False for i in range(M)]
    cols_with_zeros =[False for i in range(N)]
    for row in range(M):
        for col in range(N):
            if matrix[row][col] == 0:
                rows_with_zeros[row] = True
                cols_with_zeros[col] = True
    
    for row in range(M):
        if rows_with_zeros[row]:
            for col in range(N):
                matrix[row][col] = 0
    for col in range(N):
        if cols_with_zeros[col]:
            for row in range(M):
                matrix[row][col]= 0
    return matrix
    
