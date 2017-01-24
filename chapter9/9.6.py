#9.6
#Given a matrix in which each row and each column is
#sorted, write a method to find an element in it
def matrix_search(mat, num):
    row = 0
    col = len(mat[0])-1
    elem = mat[row][col]
    if elem == num:
        return (row, col)
    while elem != num:
        if elem > num:
            col -= 1
        elif elem < num:
            row += 1
            
        if col < 0 or row >= len(mat):
            return (-1,-1)
        elem = mat[row][col] 
        if elem == num:
            return (row, col)
        
    return (-1,-1)

#test case:
test_matrix = [[1, 4, 7, 11, 15], \
               [2, 5, 8, 12 ,19], \
               [3, 6, 9, 16, 22], \
               [10, 13, 14, 17, 24], \
               [18, 21, 23, 26, 30]]
num = 23
print(matrix_search(test_matrix, num))

