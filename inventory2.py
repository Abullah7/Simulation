#inventory lec
import random
#taking the start stk and the number of the iterations from the user
stk=int(input("Enter the intial start: "))
counter=int(input("Enter the number of iterations you want: "))
#identifing he variables which we will use
demand=0
day=1
shortage=0
End_Inventory=0
Cshortage=0
CDemand=0
CTime=0
CEnd=0
Cstk=0
ord1=0
ord2=0
dueDate1=0
dueDate2=0
for day in range(1,counter):
            #to avoid make it cumultive
            shortage=0
        #generating the RDs
            x=random.randrange(1,100,1)

           #if condition for the demand
            if 16>x>0:
                    demand=3
            elif 46>x>15:
                    demand=4
            elif 81>x>45:
                    demand=5
            elif 101>x>80:
                    demand=6
            else:
                #to know if there is an error in this part of the code
                    demand=-1
                    print("Error in Demand Code XX")
             #calc the start and end inventory
            if day>1 :
                    stk=End_Inventory
            if demand>=stk and day!=dueDate1 and day!=dueDate2:
                    shortage=demand-stk
                    End_Inventory=0
            elif stk>demand :
                    End_Inventory=stk-demand           
             
             #if condition for the lead time for order 1
            if stk<11 and dueDate1==0:
                    y=random.randrange(1,10,1)
                    print("RD for ord1 =   "+str(y))
                    if 3>y>0:
                        time=2
                    elif 9>y>2:
                        time=3
                    elif 11>y>8:
                        time=4
                    else :
                        print("Error in lead time Code XX")
                    ord1=10
                    #calc the time + the day 
                    dueDate1=time+day
             #if condition for the lead time for order 2
            elif stk<6 and dueDate2==0:
                    z=random.randrange(1,10,1)
                    print("RD for ord2 =   "+str(z))                
                    if 3>z>0:
                        time=2
                    elif 9>z>2:
                        time=3
                    elif 11>z>8:
                        time=4
                    else :
                        print("Error in lead time Code XX")
                    ord2=5
                    #calc the time + the day                    
                    dueDate2=time+day                 
            #to add the order to the inventory
            if day==dueDate1:
                 dueDate1=0
                 stk=stk+ord1
                 #to avoid calc it twice
                 if day!=dueDate2:
                           End_Inventory=stk-demand
                 ord1=0
                 #to avoid calc it twice and the pervious shortage clac it on the pervious stk so it won't work correctly
                 if demand>=stk and day!=dueDate2:
                           shortage=demand-stk
            if day==dueDate2:
                 #to avoid clac the end inventory twice
                  dueDate2=0
                  stk=stk+ord2
                  End_Inventory=stk-demand  
                  if demand>=stk:               
                            shortage=demand-stk     
                            End_Inventory=0             
                  ord2=0

        #calc the rest of the things which we will need
            Cshortage= Cshortage+shortage
            CDemand= CDemand+demand
            CEnd=CEnd+End_Inventory
            Cstk=stk+Cstk
            avg=CEnd/15
            avgDemand=CDemand/15
            avgShortage=Cshortage/15
            avgLeadTima=CTime/15
            
            
            print("Day =  "+str(day)+" |stk =  "+str(stk)+"| Cstk = "+str(Cstk)+" | ord1 = "+str(ord1)+"|due date 1 = "+str(dueDate1)+
                  " | ord2 = "+str(ord2)+"|due date 2 = "+str(dueDate2)+"| RD for Demand =  "+str(x)
                  +" |Demand =  "+str(demand)+"|Cdmd = "+str(CDemand)+" |End Inventory =  "+str(End_Inventory)
                    +" |Shortage = "+str(shortage)+" | CShortage = "+str(Cshortage))
            
            
        
print("Avg Ending inventory : "+str(avg)+" |Avg demand: "+str(avgDemand)+" |Avg lead time: "+str(avgLeadTima)+" |Avg Shortage :"+str(avgShortage))          
                                    
