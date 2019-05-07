import numpy as np
import math




def trapezium_Method(X,Y):
	n=len(X)
	sum=0
	sum=Y[0]+Y[n-1]
	for i in range(1,n-1):
		sum+=2*Y[i]
	sum= sum*(X[n-1]-X[0])/(2*(n-1))
	return sum

def Simpson(X,Y):
	n=len(X)
	sum=0
	sum=Y[0]+Y[n-1]
	a=int(n-1)
	for i in range(1, int(a/2)):
		sum+=2*Y[2*i]
	for i in range(1, int(a/2)+1 ):
		sum+=4*Y[2*i-1]
	sum= sum*(X[n-1]-X[0])/(3*(n-1))
	return sum



X=[0,math.pi/8,math.pi/4,3*math.pi/8,math.pi/2]
Y=[0,np.sin(math.pi/8),np.sin(math.pi/4),np.sin(3*math.pi/8),1]
inter=trapezium_Method(X,Y)
print(" result ",inter," error = ",1-inter)
# sin(x) '' = - sin(x) max(-sin(x))= 1 
n=len(X)
print(" expected error for sin(x) : ",pow((X[n-1]-X[0]),3)/(12*(n-1)*(n-1) ))
inter=Simpson(X,Y)
print(" SImpson result ",inter," error = ",1-inter)
# sin(x)'''' =  sin(x) max(sin(x))= 1 

print(" expected error for sin(x) : ",pow((X[n-1]-X[0]),5)/(180*pow((n-1),4) ))