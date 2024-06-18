#News dealer’s problem
import random
#identifing he variables which we will use
# take the news paper which we need to buy from the user
num=int(input("Enter the number of the news paper start with: "))
# to know the number of iterations we will work on
num2=int(input("Enter the number of the days you want : "))
#take the cost of buying , selling and scrap from the user 
costOfBuying=float(input("Enter the cost of buying: "))
costOfSelling=float(input("Enter the cost of selling to the customers: "))
costOfScrap=float(input("Enter the cost of Scrap: "))
#calc the intial payment every iteration
intialPaynent=num*costOfBuying
demand=0
Cscrap=0
Clost_profit=0
Csell=0
Cprofit=0
ProfitFromSelling=0
for day in range(1,num2+1):
        #identifing it to 0 to avoid coumultive
        lostProfit=0
        Scrap=0
        profit=0
        
        #generating the RDs
        x=random.randrange(1,100,1)
        y=random.randrange(1,100,1)
        #if condition for the type of the news
        if 31>x>0:
             p="good"
        elif 76>x>30:
             p="fair"
        elif 101>x>75:
             p="poor"
        else:
             # to know if there is error in this part of the code
             print("error in type ")
         # if condition for the probability of the news
        if p.lower()=="poor" and 41>y>0:
             demand=40
        elif p.lower()=="poor" and 66>y>40:
             demand=50
        elif p.lower()=="poor" and 81>y>65:
             demand=60
        elif p.lower()=="poor" and 93>y>80:
             demand=70   
        elif p.lower()=="poor" and 101>y>92:
            demand=80
        elif p.lower()=="fair" and 11>y>0:
             demand=40
        elif p.lower()=="fair" and 31>y>10:
             demand=50
        elif p.lower()=="fair" and 61>y>30:
             demand=60
        elif p.lower()=="fair" and 81>y>60:
             demand=70
        elif p.lower()=="fair" and 93>y>80:
             demand=80
        elif p.lower()=="fair" and 101>y>92:
             demand=90
        elif p.lower()=="good" and 5>y>0:
             demand=40
        elif p.lower()=="good" and 12>y>4:
             demand=50
        elif p.lower()=="good" and 32>y>11:
             demand=60
        elif p.lower()=="good" and 54>y>31:
             demand=70     
        elif p.lower()=="good" and 89>y>53:
             demand=80     
        elif p.lower()=="good" and 96>y>88:
             demand=90
        elif p.lower()=="good" and 101>y>95:
             demand=100    
        else:
             # to know if there is error in this part of the code
             print("error in demand ") 
        if demand>num:
             #calc lost profit
             ProfitFromSelling=num*costOfSelling
             lostProfit=(demand-num)*(costOfSelling-costOfBuying)
             Scrap=0
        elif num>demand:
             #calc Scrap
             ProfitFromSelling=demand*costOfSelling
             Scrap=(num-demand)*costOfScrap
             lostProfit=0
        elif num==demand:
             #the ideal condition
             ProfitFromSelling=demand*costOfSelling
             lostProfit=0
             Scrap=0
        else:
             # to know if there is error in this part of the code
            print("Error in lostScrap Code ")
        #calc the rest of things that we will need
        
        profit=Scrap+ProfitFromSelling-lostProfit-intialPaynent
        Cscrap=Scrap+Cscrap
        Clost_profit=lostProfit+Clost_profit
        Cprofit=profit+Cprofit
        Csell=ProfitFromSelling+Csell
        print("Day = "+str(day)+"| R.D for type = "+str(x)+ "| type of news = "+str(p)+
              "| R.D for demand = "+str(y)+"| demand = "+str(demand)+"| Revenue from sale = "+
              str(ProfitFromSelling)+"| lost profit = "+str(lostProfit)+"|gain from Scarp = "
              +str(Scrap)+"| Daily profit =  "+str(profit))
print(" sum of Revenue from sale =  "+str(Csell)+"| sum of lost profit = "+str(Clost_profit)
      +"| sum of scrap = "+str(Cscrap)+"|sum of daily profit = "+str(Cprofit))