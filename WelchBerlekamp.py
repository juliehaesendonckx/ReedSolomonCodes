from ModularGaussElimination import GaussElimination
import numpy as np
from numpy.polynomial import polynomial as Pl

def WelchBerlekamp(N,n,q,a,c):
    matrix_list = []
    e = int((N-n)/2)
    ne = n+e
    
    # Calculate G(ai) matrix
    for i in range(0,ne):
        gai = []
        for x in a:
            gai.append(pow(x,i,q))
        matrix_list.append(gai)
        
    # Calculate -yi
    yi = [(x*(-1))%q for x in c]

    # Calculate -yi*ai^ei    
    for powA in range(0,e+1):
        result = []
        for index in range(0,N):
            ai_val = pow(a[index],powA)
            r = (yi[index]*ai_val) % q
            result.append(r)
        matrix_list.append(result)
        
    matrix = np.array(matrix_list)
    naGauss = GaussElimination(matrix.T,q)
    
    noRows, noCols = naGauss.shape
    lastCol = naGauss[:, (noCols-1)]
    lastCol = [(x*(-1))%q for x in lastCol]
    
    # first 'ne' elements in the list
    gx = lastCol[:ne]

    # last 'ne' elements in the list
    ex = lastCol[ne:]
    ex.append(1)
    
    print("E(x)", ex)    
    print("G(x)", gx)    

    quotient,residu = Pl.polydiv(gx, ex)
    
    return quotient%q