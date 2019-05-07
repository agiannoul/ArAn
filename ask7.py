import numpy as np
import math
import matplotlib.pyplot as plt



def lq(V,Y,kind):
	values=V

   
	n=kind
	
	A=np.zeros((len(values),n+1))
	B=list();
	for i in range(len(values)):
		B.append(0.0);
	for i in range(len(values)):
		A[i][0]=1
		for j in range(1,n+1):
			A[i][j]=values[i]**(j)
		B[i]=Y[i];

	A=np.array(A);
	AT=A.T;

	U=np.dot(AT,A)
	V=np.dot(AT,B)
	X=np.linalg.solve(U,V);
    
	return X;

def calculatef(A,xn):
	sum=A[0]
	for i in range(1,len(A)):
		sum+=A[i]*xn**(i)
	return sum

#ethniki ETE
Y=[0.324,0.333,0.334,0.33,0.305,0.317,0.32,0.315,0.308,0.311]
Y2=[2.22,2.21,2.17,2.14,2.04,2.15,2.17,2.13,2.08,2.05]

X=[1,2,3,4,5,6,7,8,9,10]

k3=lq(X,Y,3)
k2=lq(X,Y,2)
k4=lq(X,Y,4)

a2=lq(X,Y2,2)
a3=lq(X,Y2,3)
a4=lq(X,Y2,4)
print ( " ETE ")
print(" 12 day : ")
print(calculatef(k2,12))
print(calculatef(k3,12))
print(calculatef(k4,12))
print(" 15 day : ")
print(calculatef(k2,15))
print(calculatef(k3,15))
print(calculatef(k4,15))

print ( " ALFA ")
print(" 12 day : ")
print(calculatef(a2,12))
print(calculatef(a3,12))
print(calculatef(a4,12))
print(" 15 day : ")
print(calculatef(a2,15))
print(calculatef(a3,15))
print(calculatef(a4,15))










