import numpy as np
import math
import matplotlib.pyplot as plt
def par(x,y):
    n=len(x)
    D=np.zeros((n,n))
    
    for i in range(1,n):
        D[i][1]=(y[i]-y[i-1])/(x[i]-x[i-1])
    
    for i in range(2,n):
        
        for j in range(1,n-i+1):
            D[j][i]=(D[j+1][i-1]-D[j][i-1])/(x[j+i-1]-x[j-1])
    A=np.zeros(n)
    A[0]=y[0]
    for i in range(1,n):
        A[i]=D[1][i]
    return A
    
def showPol(A,x):
    X=np.array(x)
    print("P(x)= ",A[0],end="")
    for i in range(1,len(A)):
        print("+(",A[i],")",end="")
        for j in range(i):
            print("(x-",X[j],")",end="")
#A syntelestes , a0, a1... X0 ta arxika shmeia , x o agnwstos         
def calculatePx(A,X,x):
    y=A[0]
   
    for i in range(1,len(A)):
        k=1
        for j in range(i):
            k=k*(x-X[j])
        y+=A[i]*k
    return y;


#s0 = a00 + a01x +a02x^2 +a03x^3
#==================================================SPLINES========================================

def Splines(x,y):
	n = len(x) - 1
	h = [x[i+1]-x[i] for i in range(n)]
	al = [3*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1]) for i in range(1,n)]
	a=[]
	a.append(0)
	for i in range(len(al)):
		a.append(al[i])
	al=a
  
	l =np.ones(n+1)
	u =np.zeros(n+1)
	z =np.zeros(n+1)
	for i in range(1, n):
		l[i] = 2*(x[i+1]-x[i-1]) - h[i-1]*u[i-1]
		u[i] = h[i]/l[i]
		z[i] = (al[i] - h[i-1]*z[i-1])/l[i]

	b =np.zeros(n+1)
	c =np.zeros(n+1)
	d =np.zeros(n+1)
	for i in range(n-1, -1, -1):   
		c[i] = z[i] - u[i]*c[i+1]
		b[i] = (y[i+1]-y[i])/h[i] - h[i]*(c[i+1] + 2*c[i])/3
		d[i] = (c[i+1]-c[i])/(3*h[i])
	return [y, b, c, d]
  




	
#==================================================================================================



#X=[1.0,2.0,3.0]
#Y=[8.0,5.0,10.0]


def lq(V,Y):
	values=V

   

	sin=Y;
	
	A=list()
	B=list();
	for i in range(len(values)):
		A.append(0.0);
		B.append(0.0);
	for i in range(len(values)):
		A[i]=[1,values[i],pow(values[i],2)];
		B[i]=sin[i];
	#print(A);
	A=np.array(A);
	AT=A.T;

	U=np.dot(AT,A)
	V=np.dot(AT,B)
	X=np.linalg.solve(U,V);
    
	return X;

def calculateflq(X,xn):   
	return X[0]+X[1]*xn+X[2]*xn**2
#print(calculatePx(A,X,2.79))

X=[-math.pi,-2.23,-math.pi/2,-0.36,0.0,0.69,math.pi/2,2.19,2.79,math.pi]
Y=[0.0,-0.79,-1.0,-0.352,0.0,0.637,1.0,0.814,0.344,0.0]


A1=par(X,Y)

showPol(A1,X)
print(A1,end="\n")

step=(math.pi)/100
t1 = np.arange(-math.pi, math.pi, step)
t2 = np.linspace(-math.pi, math.pi, num=200 ,endpoint=True)


Xlq=lq(X,Y)

plt.plot(t2,np.sin(t2)-calculatePx(A1,X,t2) , 'bo')

plt.plot(t1,np.sin(t1)-calculateflq(Xlq,t1) , 'ro')

a = Splines(X,Y)

  # prepare data for plotting the splines
points_per_interval = 20
xs = []
ys = []
for i in range(9):
	xs.append(np.linspace(X[i],X[i+1], points_per_interval))
	ys.append([np.sin(xs[i][k])-(a[0][i] + 
		a[1][i]*(xs[i][k]-X[i]) + 
		a[2][i]*(xs[i][k]-X[i])**2 + 
		a[3][i]*(xs[i][k]-X[i])**3)   
 		for k in range(points_per_interval)])
  


plt.plot(xs[0], ys[0], 'g.--', xs[1], ys[1], 'g.--', xs[2], ys[2], 'g.--',xs[3], ys[3], 'g.--', xs[4], ys[4], 'g.--', xs[5], ys[5], 'g.--',xs[6], ys[6], 'g.--', xs[7], ys[7], 'g.--', xs[8], ys[8], 'g.--')


plt.ylabel('error value')
plt.title("")
plt.grid()
plt.show()


