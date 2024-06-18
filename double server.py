#double
from ast import Or
from pickle import TRUE
import random
class simulation:
        Baker = 0
        Albe = 0
        Customer = 0
        h = 0
        t = 0
        t1 = 0
        t2 = 0
        time = 0

        for i in range(0, 30):
                begBaker=0
                EndBaker=0
                begAlbe=0
                endAlbe=0                
                if h >= 60:
                 break
                x = random.randrange(0, 100, 1)
                y = random.randrange(0, 100, 1)
                # IAT
                if 26>x > 0 :
                     t = 1
                elif 66>x > 25 :
                     t = 2
                elif 86>x > 65:
                     t = 3
                elif 101>x > 85:
                     t = 4
            # Baker
                if 36>y > 0:
                     t1 = 3
                elif 61>y > 35:
                     t1 = 4
                elif 81>y > 62:
                     t1 = 5
                elif 101>y > 82:
                     t1 = 6
            # ALbe
                if 31>y > 0:
                     t2 = 2
                elif 59>y > 32:
                     t2 = 3
                elif 84>y> 60 :
                     t2 = 4
                elif 101>y > 85:
                     t2 = 5

                if Customer == Baker> Albe:
                        time = t1
                        Baker = Customer+time
                        Customer = t+Customer
                        begBaker=begBaker+t
                        
                elif  Customer >= Albe> Baker:
                        time = t2
                        Albe = time +Customer
                        Customer = t+Customer
                elif Customer == Baker == Albe:
                        time = t1
                        Baker = time+Baker
                        Customer = t+Customer
                elif Customer < Baker < Albe:
                        time = t1
                        Baker = Baker+time
                        Customer = t+Customer
                elif Customer < Albe < Baker:
                        time = t2
                        Albe = time +Albe
                        Customer = t+Customer
                elif Baker == Albe or Baker < Albe and Baker != Customer:
                        time = t1
                        Baker = time+Baker
                        Customer = t+Customer
                elif Customer>=Baker>Albe:
                        time = t2
                        Albe = time +Albe
                        Customer = t+Customer
                elif Customer==Baker <Albe:
                        time = t1
                        Baker = Baker+time
                        Customer = t+Customer
                elif Albe>Customer>Baker:
                        time = t1
                        Baker = Baker+time
                        Customer = t+Customer
                elif Baker>Customer>Albe:
                        time = t2
                        Albe = time +Albe
                        Customer = t+Customer
                else:
                    print("Logic Error")
                if Albe>Baker>Customer:
                            begin=Albe
                

                h = time+h
                print("i = "+str(i)+"| clock Time:  "+str(Customer)+"| Baker service time:  "+str(Baker) +
                "|  Albe service time:   "+str(Albe)+" | total service time:   "+str(h))
            