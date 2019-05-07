import numpy
import math

def power_method (G  , p ,e):
    l1=0
    l2=l1;
    p = numpy.dot(G,p)
    
    l1=p[0][0]
   
   
    
    while True :
        l2=l1;
        p = numpy.dot(G,p)
        l1=p[0][0]
        p = (1.0/l1)*p
        if abs(l1-l2)<e :
            break
    return p

def Google(A,q):
    n=len(A)
    G=numpy.zeros((n,n))
    
    
    

    for i in range(n) :
        
        for j in range(n):
            nj=0.0
            for k in range(n) :
                nj+=A[j][k]
            G[i][j]=(q/n)+(A[j][i] * (1-q) )/nj
        
    return G
def make_sum_one(a):
    norm=0
    for i in a:
        norm+= i
    
    return (1.0/norm)*a
    
    
    
        
A=     [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
G=Google(A,0.15)
p= numpy.ones((15, 1))
k=power_method(G,p,0.00000005)
#print(k)
k=make_sum_one(k)
print(k)

A2=   [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
G=Google(A2,0.15)
p= numpy.ones((15, 1))
k=power_method(G,p,0.00000005)
#print(k)
k=make_sum_one(k)
print("we remove 4->12 we add , 15->4 14->4 ,10->4,11->4")
print(k)

#ta pososta apomakrinontai meta3h toys to q einai h pi8anothta metapidhshs se mia allh selida 
print("q=0.02")
G=Google(A2,0.02)
p= numpy.ones((15, 1))
k=power_method(G,p,0.00000005)
#print(k)
k=make_sum_one(k)
print(k)

#ta pososta vriskontai pio konta meta3h toys to q einai h pi8anothta metapidhshs se mia allh selida 
print("q=0.6")
G=Google(A2,0.6)
p= numpy.ones((15, 1))
k=power_method(G,p,0.00000005)
#print(k)
k=make_sum_one(k)
print(k)


#allazoume ton pnaka gitniashs me 3 stis syndeseis 8->11 kai 12->11
print("Change 8->11 and 8->12 to 3")
A3=   [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 3, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]   
G=Google(A3,0.15)
p= numpy.ones((15, 1))
k=power_method(G,p,0.00000005)
#print(k)
k=make_sum_one(k)
print(k)
#doulepse gia au3ish sto   pososto ths taksis toy 2% , ara uparxei au3ish kata 20% tou arxikoy posostou 




print("delete 10")
 
A4=   [[0, 1, 0, 0, 0, 0, 0, 0, 1,  0, 0, 0, 0, 0,],
       [0, 0, 1, 0, 1, 0, 1, 0, 0,  0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 1, 0,  0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0,  0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0,  1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0,  1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0,  1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0,  0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 1, 0,  1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1,  0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0,  1, 0, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 1, 0, 1, 0]]
 # to 11 ay3anetai polu kai parallila meiwnetai to 14 ka8os pleon oloi oi 
 #komvoi pou odhgoysan sto 10  den odhgoun pleon sto 14 afoy to 10 den yparxei pleon  
G=Google(A4,0.15)
p= numpy.ones((14, 1))
k=power_method(G,p,0.00000005)
#print(k)
k=make_sum_one(k)
print(k)    
       