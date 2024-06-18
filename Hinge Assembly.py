#hing
import random
#identifing the variables which we will use 
positive=0
negative=0
# to know the number of iterations we will work on
counter=int(input("Enter the number of iterations you want: "))
for i in range(counter):
        #generating RDs
        x=random.randrange(1,100,1)
        y=random.randrange(1,100,1)
        z=random.randrange(1,100,1)
        q=random.randrange(1,100,1)
        #calc a,b,c ad d
        a=1.95+.1*(x/100)
        b=1.95+.1*(y/100)
        c=29.5+(z/100)
        d=34+(q/100)
        m=a+b+c
        if m>d:
             negative=negative+1
        elif m<=d: 
              positive=positive+1
              
        print("i = "+str(i)+"| RD a = "+str(x)+"| a = "+str(a)+"| RD b ="+str(y)+"| b = "+str(b)+"| RD c = "+str(z)+"| c = "+str(c)+"| RD d = "+
              str(q)+"| d = "+str(d)+"| a+b+c = "+str(m)+"| positive = "+str(positive)+"| negative = "+str(negative))
print("+  = "+str(positive)+"|  -  = "+str(negative)+"| probability of negative = "+str((negative/counter)*100)+"| probability of positive = "+
      str((positive/counter)*100))
