from ModularGaussElimination import GaussElimination
import numpy as np

def SimpleReedSolomon(N,n,q,a,c):
    matrix_list = []

    # create the 'F' matrix
    for i in range(0,n):
        col = [pow(x,i,q) for x in a]
        matrix_list.append(col)
    matrix_list.append(c)
    matrix = np.array(matrix_list)
    
    # nxn submatrix + reult
    submatrix = matrix.T[:n,:]    
    result = GaussElimination(submatrix,q)
    lastCol = result[:, (n)]

    return lastCol