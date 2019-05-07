#include <stdio.h>
#include <stdlib.h>

double f(double x){
    double f=exp(pow(sin(x),3))+pow(x,6)-2*pow(x,4)-pow(x,3)-1;
     //printf("    f(%f) = %f \n",x,f);
    return f;

}

double f1(double x){
    double f=3*pow(sin(x),2)*cos(x)*exp(pow(sin(x),3))+6*pow(x,5)-8*pow(x,3)-3*pow(x,2);

    return f;

}
double f2(double x){
    double f=30*pow(x,4)-24*pow(x,2)-6*x-3*exp(pow(sin(x),3))*pow(sin(x),3)+6*exp(pow(sin(x),3))*sin(x)*pow(cos(x),2)+9*exp(pow(sin(x),3))*pow(sin(x),4)*pow(cos(x),2);
    return f;
}

double halfmethod(double a1,double b1,int n){
    double a=a1 , b=b1;
    int i;
    double half = (b+a)/2.0;
    if( f(a)<0 && f(b)>0){

        for( i=0;i<n;i++){
            //printf("i : %d , half = %f \n",i,half);
            if(f(half)>0){
                b=half;
            }else if(f(half)<0){
                a=half;
            }else
                return half;
            half = (b+a)/2;
        }

    }else if( f(a)>0 && f(b)<0){

        for( i=0;i<n;i++){
            //printf("i : %d , half = %f \n",i,half);
            if(f(half)>0){
                a=half;
            }else if(f(half)<0){
                b=half;
            }else
                return half;
            half = (b+a)/2;

        }
    }
    printf("   %d ", i);
    return half;
}
// h g'(x)gia elenxo tetragwnikhs syglishs
double g1(double x){
    return -(f(x)*f2(x))/(f1(x)*f1(x));
}
double Newton_Raphson(double xo){

    int i=0;
    double xn1 , xn=xo;
    char done=1;
    while(done){
        xn1 = xn - f(xn)/f1(xn);
        //printf(" xn1 = %f \n",xn1);
        if( (xn1-xn) >-0.0000005 && (xn1-xn) < 0.0000005 ){
            //printf("%f",xn1-xn);
            done=0;
        }
        xn=xn1;
        i++;
    }
    printf("   %d ", i);
    return xn;
}

double temnousa(double a1,double b1){

    int i=0;
    double xn2 , xn1 = a1 , xn=b1;
    char done=1;
    while(done){
        xn2 = xn1 - (f(xn1)*(xn1-xn))/( f(xn1) - f(xn));

        if( (xn2-xn1) >-0.0000005 && (xn2-xn1) < 0.0000005 ){

            done=0;
        }
        //printf(" %f    %f \n",xn1 , xn2 );
        xn=xn1;
        xn1=xn2;

        i++;
    }
    printf("   %d ", i);
    return xn2;
}


int main()
{

    printf(" f(-2)*f''(-2) %f \n",f(-2)*f2(-2));
    printf(" %f \n",Newton_Raphson(-2));
    printf(" %f \n",halfmethod(-2,-1,21));
    printf(" %f \n\n",temnousa(-2,-1));
    printf(" f'(-1.197624) = %f \n",f1(-1.197624));

    printf("  f(2)*f''(2) %f \n",f(2)*f2(2));
     printf(" %f \n",Newton_Raphson(2));
    printf(" %f \n",halfmethod(1.3,2,19));
    printf(" %f \n\n",temnousa(1.3,2));
    printf(" f'(1.530134) = %f \n",f1(1.530134));

    //den doulevei kamia kala
    printf(" f''(0) = %f \n",f2(0));
    printf(" f'(0) = %f \n",f1(0));
    // h f'(0) einai 0 kai h f''(0) einai 0 ara exei arketa argh siglisi
    printf(" %f \n",Newton_Raphson(0.5));

    printf(" %f \n\n",temnousa(-0.5,0.5));
    // test gia sygklish newton raphson
    printf(" g'(-1.97623)= %f \n",g1(-1.97623));
    printf(" g'(1.530133)= %f \n",g1(1.530133));



}
