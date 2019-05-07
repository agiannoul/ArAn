import math 
import random

def f(x):
	return 54*pow(x,6)+45*pow(x,5)-102*pow(x,4)-69*pow(x,3)+35*pow(x,2)+16*x-4
def f1(x):
	return 6*54*pow(x,5)+45*5*pow(x,4)-102*4*pow(x,3)-69*3*pow(x,2)+70*x+16
def f2(x):
	return 30*54*pow(x,4)+45*20*pow(x,3)-102*12*pow(x,2)-69*6*x+70



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
x=halfmethod(-0.8,-0.5)
print(" halfmethod ",x,end="\n")
print(" N_R ",Newton_Raphson(-0.8),end="\n")
print(" Secant ",Secant(-0.8,-0.7,-0.6),end="\n")
print("\n\n\n")
x=halfmethod(0.1,0.4)
print(" halfmethod ",x,end="\n")
print(" N_R ",Newton_Raphson(0.2),end="\n")
print(" Secant ",Secant(0,0.2,0.4),end="\n")
print("\n\n\n")
x=halfmethod(0.4,0.7)
print(" halfmethod ",x,end="\n")
print(" N_R ",Newton_Raphson(0.6),end="\n")
print(" Secant ",Secant(0.41,0.47,0.55),end="\n")
print("\n\n\n")
x=halfmethod(0.7,1.2)
print(" halfmethod ",x,end="\n")
print(" N_R ",Newton_Raphson(0.9),end="\n")
print(" Secant ",Secant(1,1.4,2),end="\n")

# Efarmozw ton algori8mo b) gia 10 fores sto diastima [-2,-1]
for i in range(10):
	x=halfmethod(-2,-1)
	print(" halfmethod ",x,end="\n")

