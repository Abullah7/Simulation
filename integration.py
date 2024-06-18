#integration
import random
import math
#identifing the variables which we will use 
N=0
M=0
# to know the number of iterations we will work on
counter=int(input("Enter the number of iterations you want: "))
for i in range(counter):
       #generating RDs
        x=random.randrange(1,50,1)
        y=random.randrange(1,100,1)
        #calc X,Y and X^3  
        R=(y/100)
        X=.1*x
        Y=140*R
        X_cubing=math.pow(X,3)
        if X_cubing>=Y and 140>=Y:
             N=N+1
             M=M+1
        elif X_cubing<Y and 140>=Y>=0 :
             N=N+1
        elif Y<0 or Y>140 :
             print("out of bound ")
        else:
             print("Error in fif code XXX")
        print("i = "+str(i)+"| RD for x = "+str(x)+"| X = "+str(X)+"| X^3 = "+str(X_cubing)+"| RD for y = "+str(y)+"| Y = "+str(Y)+"|M = "+
              str(M)+"| N = "+str(N) ) 
#i = (M/N)*AreaS
print(" I = "+str((M/N)*140*3))        