#inventory section
import random

class iventory:
     #taking standard level , start , order , lead time afor the order and the number of iterations as input from the user
        m=int(input("Enter the standard level: "))
        start=int(input("Enter the intial start: "))
        order=int(input("Enter the order quantity: "))
        time=int(input("Enter the lead time: "))
        counter=int(input("Enter the number of iterations you want: "))
#identifing he variables which we will use
        demand=0
       
        End_Inventory=0
        Cshortage=0
        CDemand=0
        CTime=0
        Corder=0
        CEnd=0
        y=99999999
       #counter+1 because we begginning with i=1
        for day in range(1,counter+1):
                shortage=0
             #generating RDs
                x=random.randrange(1,100,1)
                if time>-1:
                     time=time-1                
                #if condition for the demand
                if 11>x>0:
                     demand=0
                elif 36>x>10:
                     demand=1
                elif 71>x>35:
                     demand=2
                elif 92>x>70:
                     demand=3
                elif 101>x>91:
                     demand=4
                else:
                     #to know if there is an error in this part
                     demand=-1
                     print("Error in Demand Code XX")
                #to calc the start and End inventory and avoid the first iteration because it will be given
                if day>1:
                     start=End_Inventory
               # if we have an shortage
                if demand>=start and time!=-1:
                     shortage=demand-start
                     End_Inventory=0
                elif start>demand:
                      End_Inventory=start-demand
               #if condition for the order 
               # if the day equal multiples of five then order
                if (day%5)==0:
                            y=random.randrange(1,10,1)
                            order=m-(End_Inventory)
                            Corder=Corder+order
                            if 7>y>0:
                                 time=1
                            elif 10>y>6:
                                 time=2
                            elif y==10:
                                 time=3
                            else :
                           #to know if there is an error in this part
                                 
                                 print("Error in lead time Code XX")
                            CTime=CTime+time
                #make the days move

                if time==-1:
                     #when it arrive
                     start=start+order 
                     End_Inventory=start-demand
                     if demand>=start:
                               shortage=demand-start
                               End_Inventory=0
                     #time equal infinity to avoid make it 0 and think the order has arrived
                     time=999999999999   
               #calc the cumultives that we will need
                Cshortage= Cshortage+shortage
                CDemand= CDemand+demand
                CEnd=CEnd+End_Inventory
                avg=CEnd/15
                avgDemand=CDemand/15
                avgShortage=Cshortage/15
                avgLeadTima=CTime/15
                
               
                print("Day =  "+str(day)+" |start =  "+str(start)+"| RD for Demand =  "+str(x)+" |Demand =  "+str(demand)+" |End Inventory =  "+str(End_Inventory)
                      +" |Shortage = "+str(shortage)+" | order =  "+str(order)+" |RD for lead time =   "+str(y)+" |Lead time =  "+str(time)+
                "| Cumultive Demand = "+str(CDemand)+" | Cumultive order =  "+str(Corder)+" |Cumultive shortage =  "
                      +str(Cshortage)+" |Cumultive lead Time =  "+str(CTime))
                
                
                
        print("Avg Ending inventory : "+str(avg)+" |Avg demand: "+str(avgDemand)+" |Avg lead time: "+str(avgLeadTima)+" |Avg Shortage :"+str(avgShortage))          
                                    
        
                