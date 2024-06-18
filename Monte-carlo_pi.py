#pi
import random
import math
#identifing the variables which we will use 
l=0
In=0
out=0
# to know the number of iterations we will work on
counter=int(input("Enter the number of iterations you want: "))
for i in range(counter):
        #generating RDs
        x=random.randrange(1,100,1)
        y=random.randrange(1,100,1)
        #convert it to float
        R1=(x/100)
        R2=(y/100)
        #calc root(1-R1^2)
        l=math.sqrt(1-math.pow(R1,2))
        if l>=R2:
             In=In+1
        elif l<R2:
             out=out+1
        else:
             #to know if there is an eror in this part of the code
             print("Error in InOut code XXX")
        print("i = "+"| R1 = "+str(R1)+str(i)+"| R2 = "+str(R2)+"| sqrt(1-R1^2) = "+str(l)+"| in = "+str(In)+"| out = "+str(out))
pi=(In/counter)*4
print("pi = "+str(pi))        