import numpy as np
from datetime import datetime
#---------------------------------------------------------------
def mydet(A):
    """"compute deteminant of A using cofactor expansion."""
    n = A.shape[0]
    if n == 1:
        return A[0][0]
    elif n == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    else:
        det = 0
        for i in range(n):
            if A[0][i]!=0:
                minor=np.concatenate((A[1:,:i],A[1:,i+1:n+1]),axis=1)
                det+=A[0][i]*((-1)**i)*mydet(minor)
    return det
#---------------------------------------------------------------
def minor(A1,row,col):
    A1=np.delete(A1,row,0)
    A2=np.delete(A1,col,1)
    return A2
    
def mysolve_adj(A1,b1,detA):
    C = np.zeros(A1.shape)  
    nrows = C.shape[0]
    ncols = C.shape[0]
    
    for i in range(nrows):  
        for j in range(ncols):
            min=minor(A1,i,j)
            C[i,j] = ((-1)**(i+j)) * mydet(min)
    C = C.transpose()/detA
    #np.set_printoptions(precision=2)
    #print(C)
    ans = np.dot(C,b1)
    np.set_printoptions(precision=2)
    print(ans)
    return ans

#---------------------------------------------------------------
def mysolve_cramer(A, b, detA):
    X = np.zeros(b.shape) 
    C = A.copy()
    for i in range(0,len(b)):
        for j in range(0,len(b)):
            C[j][i]=b[j][0]
            if i>0:
                C[j][i-1]=A[j][i-1].copy()

        if mydet(A)!=0:
            X[i][0]=mydet(C)/mydet(A) 
        else:
            X[i][0]=0
    #print('w=%s'%X[0],'x=%s'%X[1],'y=%s'%X[2],'z=%s'%X[3])
    print(X)
    return X
#---------------------------------------------------------------
