def countOnes(mat, a, b, c, d, rows, col):
    count = 0
    if a >=0 and mat[a][c+1] == 1:    #top
        count += 1
    if b <= rows-1 and mat[b][c+1] == 1:  #bottom
        count += 1
    if c >= 0 and mat[a+1][c] == 1:       #left
        count += 1
    if d <= col-1 and mat[a+1][d] == 1:    #right
        count += 1
    return count  

def coverageOfMatrix(mat):
    count = 0
    rows = len(mat)
    col = len(mat[0])

    for i in range(rows):
        for j in range(col):
            if mat[i][j] == 0:
                count += countOnes(mat, i-1, i+1, j-1, j+1, rows, col)
    
    return count  



if __name__ == "__main__":
    mat = [[0, 1], [1, 0]]
    ans = coverageOfMatrix(mat)
    print(ans)