#single Q
import random
#identifing he variables which we will use
server=0
Customer=0
idle=0
h=0
t=0
t1=0
t2=0
time=0
Qu=0
begin=0
end=0
x=0
k=0
o=0
# to know the number of iterations we will work on
counter=int(input("Enter the number of iterations you want: "))
#counter+1 because we begginning with i=1
for i in range(1,counter+1):
       #make the idle and Q  = 0 to avoid sum it with the pervious q and idle
        Idle=0
        Queue=0
        #generating RD
        z=random.randrange(0,100,1)
        
        #IAT
        #make I>1 because the first iteration doesn't need IAT
        if i>1: 
                    x=random.randrange(0,100,1)
                    if 26>x>0 :
                              t=1
                    elif 66>x>25:
                              t=2 
                    elif 86>x>65:
                              t=3 
                    elif 101>x>85:
                              t=4
        #Customer=clock Time       
        Customer=Customer+t  
        #clac the begin 
        #server=end
        if Customer>=server :
             #if the clock time>the last end  then we start with clock time as the begin
                begin=Customer
        elif Customer<server :
               #if the clock time<the last end  then we start with the last end as the begin
                begin=server
        
        #server
        
        if 31>z>0:
                t2=1
        elif 59>z>30:
                 t2=2
        elif 84>z>58:
                t2=3
        elif 101>z>83:
                t2=4
         #calc the idle , Queue and end  
        if server<=Customer:
                    Idle=(Customer-server)
                    server=t2+Customer

                  
        elif server>Customer:
                    time=t2
                    #if condition to avoid calc Queue in the first iteration 
                    if Customer!=0:
                          Queue=(server-Customer)
                    
                    server=server+t2

        else:
             print("Logic Error")
        if Idle!=0:
             k=k+1
        elif Queue!=0:
              o=o+1
        
        idle=Idle+idle
        Qu=Qu+Queue
    
        print("i = "+str(i)+"| clock Time = "+str(Customer)+"| RDIAT = "+str(x)+"| IAT = "+str(t)+
              "|begin = "+str(begin)+"| RDST = "+str(z)+"| service time = "+str(t2)+
              "|end = "+str(server)+" | total service time = "+str(h)+"| Queue = "+str(Queue)+"| idle = "+str(Idle))
        if h>=60:
             break
print("sum of idle = "+str(idle)+"| sum of Queue = "+str(Qu)+"| Avg waiting time = "+str(Qu/(counter+1))+"|probability wait =  "+str(o/(counter+1))+
      "| Avg idle server =  "+str(idle/(counter+1))+"| probability idle = "+str(k/(counter+1)))