from ModularInverse import ModularInverse

def Pivot(row,i,m):
    inverse = ModularInverse(int(row[i]),m)
    row = (row*inverse)%m
    return row 



def GaussElimination(A, p):
    i = 0
    N, n = A.shape
        
    for i in range(N):
        col = i
        A[i] = Pivot(A[i],i,p)
        for j in range(N):
            if (j != i):
                A[j] =( A[j]-((A[i]*A[j][col])%p))%p
                
    return A%p