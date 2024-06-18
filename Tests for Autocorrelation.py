#autocorrelation
import math
# to know the number of RDs we work on
counter=int(input("Enter the number of R.D: "))
#to know the Z a/2 to make the test 
ZalphaOver2=float(input("Enter the Z alpha/2: "))
MenusZalphaOver2=float(input("Enter the -Z alpha/2: "))
RD=[]
wanted=[]
SegmaRow=0
t1=0
t2=0
ROW=0
#put the RD into a list
for i in range(counter):
      p=float(input("Enter the RD :"))
      RD.append(p)
#to know the RD which we need test
counter2=int(input("Enter the number of R.D you want to test on: "))
for i in range(counter2):
      p=int(input("Enter the RD index:"))
      wanted.append(p)
#to calculate i = the first number (in the numbers we want to test)      
u=wanted[0]  
#calculate m (jump)
leg=abs(wanted[1]-wanted[0])
#calculate M and floor it because it should be integer
M=math.floor(((len(RD)-u)/leg)-1)
#numerator
t1=float(math.sqrt(13*M+7))
#denominator
t2=float(12*M+12)
SegmaRow=abs(float(t1/t2))
#calc the Segma Row
for i in range(u,len(RD),leg):
     print("i = "+str(i))
     if i+leg>=len(RD):
         break
     else:
            Row=(1/(M+1))*(RD[i]*RD[i+5])-0.25
#clac the Z          
Z0=(Row/SegmaRow)
print("leg = "+str(leg)+"| M = "+str(M)+"| segma Row = "+str(SegmaRow)+"| Row = "+str(Row)+"| Z node = "+str(Z0))
#doing the test
if ZalphaOver2>Z0>MenusZalphaOver2:
       print(" Fail to reject")
else:
       print("rejected")     
     