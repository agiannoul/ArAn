import numpy

def swap(A,i,pos):
    n=len(A)
    Temp=numpy.ones(n)
    for j in range(n):
        Temp[j]=A[i][j]
        A[i][j]=A[pos][j]
        A[pos][j]=Temp[j]
    return A

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

def pa_lu(A1,b):
    n=len(A1)
    P=numpy.identity(n)
    L=numpy.zeros((n,n))
    A=numpy.array(A1)
    pos=0
    l=0.0
    for j in range(n-1):
       
        #vriskei to max sthn j stilh 
        maxx=abs(A[j][j])
        for i in range(j,n):
            if maxx<abs(A[i][j]):
                maxx=abs(A[i][j])
                pos=i
        
        #antimeta8eto thn grammi j me thn pos 
        A=swap(A,j,pos)
        P=swap(P,j,pos)
        L=swap(L,j,pos)
        #mhdenizei to prwto stoixeio ka8e grammhs katw apo thn j
        for k in range(j+1,n):
            print(A)
            l= (A[k][j]/(1.0*A[j][j]))
            
            L[k][j]=l
            for q in range(j,n):
                A[k][q]=A[k][q]-l*A[j][q]
       
    U=A
    L=L+numpy.identity(n)
    print(U)
    print(L)
    #-------------- L Y = Pb
    b=numpy.dot(P,b)
    Y = numpy.zeros(n)
    
    Y=down_triangle(L,Y,b)
    print(Y)
    #------------- Ux=Y

    
    X = numpy.zeros(n)
    
    X=up_triangle(U,X,Y)
    
    #----------------------------------
    
    return X.T
    
    
 #============TEST====================
A=[[ 1. , 2. ,  3. , 1.],
   [ 4. , 5. ,  6. , 1.],
   [ 7. , 8. ,  9. , 1.],
   [ 5. , 2. ,  3. , 1.]]

b=[[7] , [16],[25] ,[11] ]

x=pa_lu(A,b)
print(x)