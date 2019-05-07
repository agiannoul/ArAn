import numpy

def gauss_Seidel(A,b):
    n=len(A)
    xp=numpy.zeros(n)
    xa=numpy.zeros(n)
    
    while True :
        xp=numpy.array(xa)
        for i in range(n):
            xa[i]=b[i]/A[i][i]
         
            for j in range(n):
                if j != i and  A[i][j] != 0 :
                    xa[i]-=(xa[j]*A[i][j])/A[i][i]
        if numpy.linalg.norm(numpy.subtract(xa, xp), numpy.inf)<0.00005:
            break
    return xa
    
    
def Make_A(n):
    A=numpy.zeros((n,n))
    for i in range(n):
        A[i][i]=5
    for i in range(n-1):
        A[i + 1][i]=-2
        A[i][i+1]=-2
    print("Make A")
    return A
def Make_b(n):
    b=numpy.ones(n)
    b[0]=3
    b[n-1]=3
    print("Make Β")
    return b
    
    

n=10
A=Make_A(n)
b=Make_b(n)
#print(A)
#print(b)
x=gauss_Seidel(A,b)
print(x)
print(numpy.dot(A,x))