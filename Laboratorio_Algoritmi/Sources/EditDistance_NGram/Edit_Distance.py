def Edit_Distance(word1, word2):
    mat = [ [ 0 for i in range(len(word1) +1) ] for j in range(len(word2) +1) ]
    
    for i in range(len(word2) + 1):
        mat[i][0] = i
    
    for j in range(len(word1) + 1):
        mat[0][j] = j
    
    for i in range(1, len(word2) +1):
        for j in range(1, len(word1) +1):
            if word1[j-1] == word2[i-1]:
                mat[i][j] = mat[i-1][j-1]
            else:
                mat[i][j] = min(mat[i-1][j],
                                mat[i-1][j-1],
                                mat[i][j-1]) +1
    
    print(mat)
    return mat[len(word2)][len(word1)]