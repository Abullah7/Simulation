#Linear Congruential Method
#Z node
intialStart=int(input("Enter the intial start:"))
Modulus=int(input("Enter the modulus: "))
a=int(input("Enter the value of a: "))
#it can be 0
c=int(input("Enter the value of c: "))
#calc Z1
Z=(a*intialStart+c)%Modulus
print(str(Z/Modulus))
#identifing Z2 with infinty number to it be immpossible to be RD and not identifing it to  0 cause 0 can be RD  
Z2=99999999999999999999999999999
for i in range(0,99999):
    #to stop in modulus-1 in order to not repeat
        if Z2==intialStart:
            break
# i didn't use Z node in the equation cause i will use it in the break condition (to not changing its value)
        Z2=(a*Z+c)%Modulus
        Z=Z2
        #Ri=Zi/m
        print(Z2/Modulus)

     
