#Kolmogorov-Smirnov Test
from array import *
# to know the number of RDs we work on
counter=int(input("Enter the number of R.D: "))
#to know the D alpha to make the test
D_alpha=float(input("Enter D alpha: "))
#identifing the variables we work on
F=[]
Sn=[]
diff=[]
#put the RD into a list
for i in range(counter):
      p=float(input("Enter the RD Digits:"))
      F.append(p)
#sorting it
F.sort()
for i in range(len(F)):
            #i+1 because the first iteration is 0
            s= (i+1)/len(F)
            # put it into a list
            Sn.append(s)
            #calc the difference
            d=Sn[i]-F[i]
            #take the absulte value of it
            diff.append(abs(d))
#printing
for i in range(len(Sn)):
      print("F =  "+str(F[i])+"| Sn =  "+str(Sn[i])+"| diff =  "+str(diff[i]))
#take the max value
max=max(diff)
print("max = "+str(max))
#doing the test
if max>D_alpha:
       print(" rejected")
elif max<=D_alpha:
       print("Fail to reject")
