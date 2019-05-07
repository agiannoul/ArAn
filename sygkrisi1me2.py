import math 
import random
import numpy as np
def f(x):
	return np.exp(pow(np.sin(x),3))+pow(x,6)-2*pow(x,4)-pow(x,3)-1
def f1(x):
	return 3*pow(math.sin(x),2)*math.cos(x)*np.exp(pow(math.sin(x),3))+6*pow(x,5)-8*pow(x,3)-3*pow(x,2);
def f2(x):
	return 30*pow(x,4)-24*pow(x,2)-6*x-3*np.exp(pow(math.sin(x),3))*pow(math.sin(x),3)+6*np.exp(pow(math.sin(x),3))*math.sin(x)*pow(math.cos(x),2)+9*np.exp(pow(math.sin(x),3))*pow(math.sin(x),4)*pow(math.cos(x),2);



def r( xn2, xn1):
	return f(xn2)/f(xn1);


def q( xn, xn1):
	return f(xn)/f(xn1);


def s( xn2, xn):
	return f(xn2)/f(xn);

def halfmethod(a, b):

	
	i=0
	if f(a)<0 and f(b)>0 :
		while True:
			half=random.uniform(a,b)
			i+=1 
			
			if f(half)>0:
				b=half
			elif f(half)<0:
				a=half
			if b-a<5*pow(10,-7) and b-a>-5*pow(10,-7):
				print(" loops : ",i,end="")
				return half

	elif f(a)>0 and f(b)<0 :
		while True:
			half=random.uniform(a,b)
			
			i+=1 
			if f(half)>0:
				
				a=half
			elif f(half)<0:
				
				b=half
			if b-a<5*pow(10,-7) and b-a>-5*pow(10,-7):
				print(" loops : ",i,end="")
				return half
	print(" Bolzano has no power here")
	return -999
    
def Newton_Raphson(x):
	x0=x
	Xn=0
	i=0
	while(True):
		Xn = x0-f(x0)/f1(x0)-0.5*f(x0)*f(x0)*f2(x0)/f1(x0)**3
		if abs(Xn - x0) < 5 * pow(10, -7):
			break
		x0 = Xn
		i += 1
	print("loops : ", (i))
	return Xn

def Secant(a, b ,c):
	Xn  = a
	Xn1 = c
	Xn2 = b
	Xn3 = 0
	q1 = q(Xn,Xn1)
	r1 = r(Xn2,Xn1)
	s1 = s(Xn2,Xn)
	i = 0
	while (True):
		Xn3 = Xn2 -(r1*(r1-q1)*(Xn2-Xn1)+(1-r1)*s1* (Xn2-Xn))/((q1-1)*(s1-1)*(r1-1))
		if abs(Xn3 - Xn2) < 5 * pow(10, -7):
			break
		Xn = Xn1
		Xn1 = Xn2
		Xn2 = Xn3
		q1 = q(Xn,Xn1)
		r1 = r(Xn2,Xn1)
		s1 = s(Xn2,Xn)
		i += 1
	print("loops : ", (i))
	return Xn3


x=halfmethod(-2,-1)
print(" halfmethod ",x,end="\n")
print("  N_R ",Newton_Raphson(-2),end="\n")
print(" Secant ",Secant(-1.5,-1.3,-1.2),end="\n")
print("\n\n\n")

x=halfmethod(1.3,2)
print(" halfmethod ",x,end="\n")
print(" N_R ",Newton_Raphson(2),end="\n")
print(" Secant ",Secant(1.3,1.7,2),end="\n")
print("\n\n\n")


