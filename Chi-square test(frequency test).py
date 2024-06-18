#Chi Square
#identifing the variables we will use
RD=[]
O=[]
O1=0
O2=0 
O3=0
O4=0
O5=0
O6=0
O7=0
O8=0
O9=0
O10=0
diff=[]
sq=[]
result=[]
sumRESULT=0
sumOI=0
sumDiff=0
sumPow=0
# to know the number of RDs we work on
counter=int(input("Enter the number of R.D: ")) 
#to know the chi square to make the test
alpha=float(input("Enter the value of chi from the table : "))
#put the RD into a list
for i in range(counter):
      p=int(input("Enter the RD :"))
      p=p/100
      RD.append(p)
#calc Ei
Ei=(len(RD)-1)/10
#if condition to clac Oi
for i in range(len(RD)):
     if 0.1>RD[i]>=0:
         O1=O1+1
     elif 0.2>RD[i]>=0.1:
         O2=O2+1
     elif 0.3>RD[i]>=0.2:
         O3=O3+1
     elif 0.4>RD[i]>=0.3:
          O4=O4+1
     elif 0.5>RD[i]>=0.4:
          O5=O5+1
     elif 0.6>RD[i]>=0.5:
          O6=O6+1
     elif 0.7>RD[i]>=0.6:
          O7=O7+1
     elif 0.8>RD[i]>=0.7:
          O8=O8+1
     elif 0.9>RD[i]>=0.8:
          O9=O9+1
     elif 1>RD[i]>=0.9:
          O10=O10+1
     else:
          #to know if there is an error in this part
          print("Error in OI code XXX") 
#put Oi into a list to make it easy to use 
O.append(O1)
O.append(O2)
O.append(O3)
O.append(O4)
O.append(O5)
O.append(O6)
O.append(O7)
O.append(O8)
O.append(O9)
O.append(O10)
for i in range(len(O)):
        #clac O[i]-Ei
        d=O[i]-Ei
        diff.append(abs(d))
         #(O[i]-Ei)^2
        f=pow(d,2)
       #put it into a list to print it
        sq.append(f)
         #((O[i]-Ei)^2)/Ei 
        y=f/Ei
         #put it into a list to print it
        result.append(y)
          # printing chi square node
        sumRESULT=sumRESULT+y
        #printing sum of Oi
        sumOI=sumOI+O[i]
          #printing sum of (Oi-Ei)  
        sumDiff=sumDiff+d
        #printing sum of ((O[i]-Ei)^2)/Ei
        sumPow=sumPow+f
        print("interval = "+str(i+1)+"| O"+str(i+1)+" = "+str(O[i])+"| Ei = "+str(Ei)+"| Oi-Ei = "+str(diff[i])+
              "|(Oi-Ei)^2 = "+str(sq[i])+"| (Oi-Ei)^2/Ei = " +str(result[i]) )
print("sum of  Oi = "+str(sumOI)+"| sum of Oi-Ei = "+str(sumDiff)+"| sum of (Oi-Ei)^2 = "+str(sumPow)+"| sum of (Oi-Ei)^2/Ei =  "+
      str(sumRESULT))    
#doing the test      
if sumRESULT>alpha:
       print(" rejected")
elif sumRESULT<=alpha:
       print("Fail to reject")     
     
            