#Random Walk
import random
#identifing the variables which we will use 
forward=0
left=0
right=0
# to know the number of iterations we will work on
counter=int(input("Enter the number of iterations you want: "))
for i in range(counter):
        #generating RDs
        x=random.randrange(1,10,1)
        # if condition to calc the position
        if 6>x>0:
             forward=forward+1
        elif 9>x>5:
             left=left+1
        elif 11>x>8:
             right=right+1
        else:
             # to know if there is an error in this part
             print("Error in if code XXX")
        print("RD = "+str(x)+"|"+"("+str(forward)+","+str(right-left)+")")