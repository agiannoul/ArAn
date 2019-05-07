import numpy
import math
'''
#Fuctions to solve LY=b and LT x = Y ...


def down_triangle(L,Y,b):
    n=len(L)
    for i in range(n):
        Y[i]=b[i]/(1.0*L[i][i])
        
        for j in range(0,i):
            
            Y[i]-=(Y[j]*(1.0*L[i][j]))/L[i][i]
    return Y

def up_triangle(U,X,Y):
    n=len(U)
    for i in range(n):
        X[n-i-1]=Y[n-i-1]/U[n-i-1][n-i-1]
        
        
        for j in range(0,i):
            
            X[n-i-1]-=(X[n-j-1]*(1.0*U[n-i-1][n-j-1]))/U[n-i-1][n-i-1]
    return X

'''
def cholesky(A):
    n=len(A)
    L=numpy.zeros((n,n))
    for j in range(n):
        L[j][j]=A[j][j] 
        
        for q in range(0,j):
            L[j][j]-=L[j][q]*L[j][q]
            
        L[j][j]=math.sqrt(L[j][j])
        
        for i in range(j+1,n):
            
            L[i][j]=A[i][j]
            for q in range(0,j):
                L[i][j]-=L[j][q]*L[i][q]
            L[i][j]=1.0*L[i][j]/L[j][j]
            
    return L
    
    
A=[[1, 2, 3],
   [2, 8,22],
   [3,22,82]]
    
G=cholesky(A)


print(G)
    
    