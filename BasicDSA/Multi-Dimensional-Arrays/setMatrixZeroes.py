# Approach : 1
def setZeros1(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    dummy1 = [-1] * rows
    dummy2 = [-1] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                dummy1[i] = 0
                dummy2[j] = 0

    for i in range(rows):
        for j in range(cols):
            if dummy1[i] == 0 or dummy2[j] == 0:
                matrix[i][j] = 0

    return matrix

# Approach 2

def setZeros2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    col0 = False
    for i in range(rows):
        if matrix[i][0] == 0:
            col0 = True
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0:
            matrix[i][0] = 0
        
    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [0, 1, 1]]
    matrix1 = [[1, 1, 1], [1, 0, 1], [0, 1, 1]]
    ans = setZeros1(matrix)
    print(ans)
    ans1 = setZeros2(matrix1)
    print(ans1)
