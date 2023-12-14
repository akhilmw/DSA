def isMatrixSymmetric(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True




if __name__ == "__main__":
    mat = [[1, 2, 3], [2, 4, 5], [3, 5, 8]]
    ans = isMatrixSymmetric(mat)
    print(ans)