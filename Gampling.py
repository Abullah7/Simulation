#Gambling Game
import random
#identifing the variables which we will use 
head=0
tail=0
#if the difference equal 3 it will be raise
win=0
# to know the number of iterations we will work on
counter=int(input("Enter the number of iterations you want: "))
for i in range(counter):
        #generating RD
        x=random.randrange(0,10,1)
        if 5>x>-1:
            head=head+1
        elif 10>x>4:
            tail=tail+1
        else:
            #to know if there is an error in this part
            print("error  in HeadTail code XXX")
        if abs(head-tail)==3:
           #know if the player wins 
            win=8+win
        print("i = "+str(i)+"| RD = "+str(x)+"| head = "+str(head)+"| tail = "+str(tail)+"| Win = "+str(win))
#calc the total profit
profit=win-counter
print("profit = "+str(profit))