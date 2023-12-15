def transposeMatrix(mat):
    rows = len(mat)
    for i in range(rows):
        for j in range(i+1, rows):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def inplaceRotate(mat):
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        reverse(mat[i], 0, cols-1)
    transposeMatrix(mat)
    return mat




if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans = inplaceRotate(matrix)
    print(ans)