

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import sys
import time

cn=mysql.connector.connect(user="root",password="root",host="localhost",charset="utf8")
con=cn.cursor()
con.execute("use railway")
con.execute("drop table passenger_login;")
con.execute("create table passenger_login(username varchar(20),PASSWORD varchar(30),AGE int(3), PHONE_NO char(10));")
con.execute("drop table passenger_detail;")
con.execute("create table passenger_detail(PNR_NO int,username varchar(20),TRAIN_NO int,FROM_ varchar(20) ,TO_ varchar(20),CLASS char(4),NO_OF_TICKETS int);")
print("-*"*55)
#Importing data using csv
df=pd.read_csv("C:\\Users\\jyoti\\Desktop\\DS\\train_data.csv",index_col="TRAIN_NO")
#Adding a row
df.loc[12220]=["Kathgodam","Jammu","Jammu Garib Rath","6:30 PM","9:30 PM","783km",935,898,685,"15hr42min"]
#Adding a column
df["AC-3"]=2000
#Deleting a row/column
df=df.drop(["AC-3"],axis=1)

print("""
                                +---------------------------------------------------+
                                |                WELCOME TO                         |
                                +---------------------------------------------------+
                                | Indian  Railway  Reservation  Program             |
                                +---------------------------------------------------+
      """)
def func1():   
    print("-*"*55)
    m2=print("""
                                         +-----------------------------+
                                         |         MENU                |
                                         +-----------------------------+
                                         | Enter 1: Sign Up            |
                                         | Enter 2: Login              |
                                         | Enter 3: Exit Program       |
                                         +-----------------------------+
        """ )
    print("-*"*55)
    userinput=int(input("Please select any of the above option:"))
    #function to exit
    def func5():
            print()
            inplast=str(input("Do you really want to exit? (Y/N)\nEnter Y for Yes and N for No:"))
            if inplast=="y" or inplast=="Y":
                print()
                print("-*"*55)
                print("""
                                +----------------------------------------------------+
                                |Thank  you  for  visiting  our  program!            |
                                +----------------------------------------------------+
                    """)
                print("-*"*55)
            elif inplast=="N" or inplast=="n":
                print()
                print("!!!Thank you for continuing with our program!!!")
                print()
                func1()
            else:
                print()
                print("!!!Please enter from given options only!!!")
    
    if userinput==1:
        def func2():
            inp1=str(input("Enter your username:"))
            inp1=inp1.title()
            inp2=str(input("Enter password:"))
            inp3=int(input("Enter your age:"))
            inp4=int(input("Enter your phone number:"))
            insertrow=("insert into passenger_login (username,password,age,phone_no) values(%s,%s,%s,%s);")
            data=(inp1,inp2,inp3,inp4)
            con.execute(insertrow,data)
            cn.commit()
            print("..................................LOADING............................................")
            time.sleep(0.5)
            print()
            print("-*"*55)
            print()
            print("Account created successfully..")
            print()
            print("-*"*55)
            def func3():
                print()
                print("+"+"-"*120+"+")
                print("*"*30+"-"*5+'WECOME '+inp1+"-"*5+"*"*30)                    
                print("+"+"-"*120+"+")
                print("""
                        +----------------------------------------+
                        |               MENU                     |
                        +----------------------------------------+
                        | Enter 1: Book a Ticket                 |  
                        | Enter 2: Rail Enquiry                  |
                        | Enter 3: Report Issue                  |
                        | Enter 4: View Statistics               |
                        | Enter 5: Log Out                       |
                        +----------------------------------------+
                         """ )
                print("-*"*60)
                print()
                inp5=int(input("Please select any of the above option:"))
                def func4():
                    print("""
                        +--------------------------------------+
                        | Enter 1: To go to menu        |
                        | Enter 2: To exit the program|
                        +--------------------------------------+
                            """)
                    print()
                    opt=int(input("Enter any of the above option:"))
                    print()
                    if opt==1:                            
                        func3()
                    elif opt==2:
                        func5()
                    else:
                        print()
                        print("!!!Please enter from given options only!!!")
                if inp5==1:
                    print()
                    print("The Train details are:")
                    print()
                    print(df.iloc[0:10,0:4])
                    print()
                    print(df.iloc[0:10,4:12])
                    print()
                    print("Kindly fill the details given below from the above tables.")
                    print()
                    inp5_1=str(input("Enter your full name:"))
                    inp5_1=inp5_1.title()
                    gen=str(input("Enter your gender('F' For Female/'M' for Male):"))
                    gen=gen.title()
                    inp5_2=int(input("Enter your desired Train no.:"))
                    inp5_3=df.at[inp5_2,"FROM"]
                    inp5_4=df.at[inp5_2,"TO"]
                    mnth=str(input("Enter month of journey:"))
                    dte=int(input("Enter date of journey:"))
                    yr=int(input("Enter year of journey:"))
                    print("""
                            Enter Ac1- For AC first class
                            Enter Ac2- For AC second class
                            Enter Slp- For sleeper class
                            """)
                    inp5_7=str(input("Enter your desired class from above options:"))
                    inp5_7=inp5_7.title()
                    inp5_6=int(input("Enter PNR no.(By server):"))
                    amt=df.at[inp5_2,inp5_7]
                    insertrow1=("insert into passenger_detail (pnr_no,username,train_no,from_,to_,class) values(%s,%s,%s,%s,%s,%s);")
                    data1=(inp5_6,inp1,inp5_2,inp5_3,inp5_4,inp5_7)
                    con.execute(insertrow1,data1)
                    cn.commit()
                    print()
                    print("-*"*60)
                    print()
                    print("...............PLEASE WAIT WHILE YOUR TICKET IS BEING GENERATED...................")
                    time.sleep(0.8)
                    print("+"+"-"*128+"+")
                    print("|------Happy Journey!----------------------INDIAN RAILWAY----------------Happy Jorney!----------------|")
                    print("|----------------------------------------------RESERVATION TICKET-----------------------------------------------|")
                    print("+"+"-"*128+"+")
                    print("PNR NO.:",inp5_6,"                         ","Passenger Name.:",inp5_1)
                    print("Phone No.:",inp4,"                  ","Age:",inp5_6)
                    print("GENDER:",gen,"                               ","Date of journey:",yr,"-",mnth,"-",dte)
                    print("Departure Time:",df.at[inp5_2,"DEPARTURE"],"                ","Arrival Time:",df.at[inp5_2,"ARRIVAL"])
                    print("FROM:",inp5_3,"                        ","TO:",inp5_4)
                    print("Class:",inp5_7,"                                  ","Amount:",amt)
                    print("+"+"-"*128+"+")
                    func4()
                elif inp5==2:
                    print()
                    print("The Train details are:")
                    print("-*"*60)
                    print(df.iloc[0:10,0:4])
                    print()
                    print(df.iloc[0:10,4:7])
                    print()
                    print(df.iloc[0:10,7:11])
                    print()
                    print("-*"*60)
                    print("More routes will be updated soon..")
                    print("-*"*60)
                    func4()
                elif inp5==3:                        
                    print()
                    issue=str(input("Please give a brief description of the issue you are facing.:"))
                    print()
                    print("-*"*60)
                    print("...Thankyou for your valuable input..." )
                    print()
                    print("...Sorry for inconvenience...")
                    print()
                    print("-*"*60)
                    print("")
                    func4()
                elif inp5==4:
                    def statistics():
                        print()
                        print("""
                            +---------------------------------------------------------------------------+
                            |                               STATISTICS MENU                             |
                            +------------------------------------------------------ --------------------+
                            |Enter 1:To view statistical data showing time taken by different routes    |
                            |Enter 2:To view statistical data showing cost variation in class           |
                            |Enter 3:To view statistical data showing distance covered in each route    |
                            +---------------------------------------------------------------------------+
                                     """)
                        stats=int(input("Please enter any of the given option:"))
                        if stats==1:
                            print("The tabular data is given below:")
                            print()
                            print(df.loc[:,"HRS"])
                            print()
                            print("-*"*60)
                            print()
                            print("You can view the graph of the data from Plots pane")
                            print()
                            #Line Chart
                            z2=['12055','12017','14041','12210','12092','15036','15056','22976','5313','12220']
                            x2=[555,755,2715,11450,824,640,626,2325,625,1542]
                            plt.plot(z2,x2,'cyan',linestyle='dashed',marker='d',markeredgecolor='red')
                            plt.xlabel("Train No.")
                            plt.ylabel("Time taken")
                            plt.title("Graph showing time taken by different routes")
                            plt.show()
                            func4()
                        elif stats==2:
                            print("The tabular data is given below:")
                            print()
                            print(df.iloc[0:10,6:9])
                            print()
                            print("-*"*60)
                            print()
                            print("You can view the graph of the data from Plots pane")
                            print()
                            #Multiple Bar Chart
                            plt.figure(figsize=(10,7))
                            trn1=[750,830,325]
                            trn2=[745,865,335]
                            trn3=[1346,1265,560]
                            trn4=[1390,1315,654]
                            trn5=[550,730,220]
                            trn6=[625,780,280]
                            trn7=[665,795,225]
                            trn8=[1595,1452,710]
                            trn9=[665,796,225]
                            trn10=[935,898,685]
                            Class=['AC-1','AC-2','Slp']
                            x=np.arange(len(Class))
                            plt.bar(Class,trn1,width=0.07,label='train_12055')
                            plt.bar(x+0.05,trn2,width=0.07,label='train_12017')
                            plt.bar(x+0.10,trn3,width=0.07,label='train_14041')
                            plt.bar(x+0.15,trn4,width=0.07,label='train_12210')
                            plt.bar(x+0.20,trn5,width=0.07,label='train_12092')
                            plt.bar(x+0.25,trn6,width=0.07,label='train_15036')
                            plt.bar(x+0.30,trn7,width=0.07,label='train_15056')
                            plt.bar(x+0.35,trn8,width=0.07,label='train_22976')
                            plt.bar(x+0.40,trn9,width=0.07,label='train_5313')
                            plt.bar(x+0.45,trn10,width=0.07,label='train_12220')
                            plt.legend(loc='upper right')
                            plt.xlabel("Class")
                            plt.ylabel("Cost as per different trains")
                            plt.title("Graph showing cost variation in class")
                            plt.show()
                            func4()
                        elif stats==3:
                            print("The tabular data is given below:")
                            print()
                            print(df.loc[:,"DISTANCE"])
                            print()
                            print("-*"*60)
                            print()
                            print("You can view the graph of the data from Plots pane")
                            print()
                             #Bar Chart
                            print(df.iloc[0:9,0:3])
                            x1=['12055','12017','14041','12210','12092','15036','15056','12527','5313','12220']
                            y2=[315,336,1104,1153,187,237,253,1175,255,783]
                            plt.bar(x1,y2,color='m')
                            plt.xlabel("Train No.")
                            plt.ylabel("Distance")
                            plt.title("Graph showing distance covered in each route")
                            plt.show()
                            func4()
                        else:
                            print("Please enter from given options only.")
                            statistics()
                    statistics()              
                elif inp5==5:                                                   
                    print()
                    log1=str(input("Do you really want to logout? (Y/N)\nEnter Y for yes and N for No:"))
                    print()
                    if log1=="y" or log1=="Y":                             
                        print("-*"*60)
                        print("""
                            ...Thankyou for logging in with us...
                            """)
                        print("-*"*60)
                        func1()
                    elif log1=="n" or log1=="N":
                        print("-*"*60)
                        print(("""
                                 ...Thankyou for rejoining with us...
                                """))
                        print("-*"*60)
                        func4()
                else:                                                    
                        print("!!!Please enter from given options only!!!")
                        print()
                        func3()            
            func3()
        func2()    
   
    elif userinput==2:
        def func6():
            inp1=str(input("Enter username:"))
            inp1=inp1.title()
            inp2=str(input("Enter your password:"))
            con.execute("select username,password from passenger_login")
            for (username,password) in con:
                if inp1==username:
                    if inp2==password:
                        print("......................LOGGING IN.....................")
                        time.sleep(0.8)
                        print("..............Successfully logged in...................")                       
                        print()
                        def func3():
                            print()
                            print("+"+"-"*120+"+")
                            print("*"*30+"-"*5+'WECOME '+inp1+"-"*5+"*"*30)                    
                            print("+"+"-"*120+"+")
                            print("""
                                                     +----------------------------------------+
                                                     |               MENU                     |
                                                     +----------------------------------------+
                                                     | Enter 1: Book a Ticket                 |  
                                                     | Enter 2: Rail Enquiry                  |
                                                     | Enter 3: Report Issue                  |
                                                     | Enter 4: View Statistics               |
                                                     | Enter 5: Log Out                       |
                                                     +----------------------------------------+
                                         """ )
                            print("-*"*60)
                            print()
                            inp5=int(input("Please select any of the above option:"))
                            def func4():
                                print("""
                                          +--------------------------------------+
                                          | Enter 1: To go to menu        |
                                          | Enter 2: To exit the program|
                                          +--------------------------------------+
                                             """)
                                print()
                                opt=int(input("Enter any of the above option:"))
                                print()
                                if opt==1:
                                    func3()
                                elif opt==2:
                                    func5()
                                else:
                                    print()
                                    print("!!!Please enter from given options only!!!")
                            if inp5==1:
                                print()
                                print("The Train details are:")
                                print()
                                print(df.iloc[0:10,0:4])
                                print()
                                print(df.iloc[0:10,4:12])
                                print()
                                print("Kindly fill the details given below from the above tables.")
                                print()
                                inp5_1=str(input("Enter your full name:"))
                                inp5_1=inp5_1.title()
                                gen=str(input("Enter your gender('F' For Female/'M' for Male):"))
                                gen=gen.title()
                                inp5_2=int(input("Enter your desired Train no.:"))
                                inp5_3=df.at[inp5_2,"FROM"]
                                inp5_4=df.at[inp5_2,"TO"]
                                mnth=str(input("Enter month of journey:"))
                                dte=int(input("Enter date of journey:"))
                                yr=int(input("Enter year of journey:"))
                                print("""
                                            Enter Ac1- For AC first class
                                            Enter Ac2- For AC second class
                                            Enter Slp- For sleeper class
                                          """)
                                inp5_7=str(input("Enter your desired class from above options:"))
                                inp5_7=inp5_7.title()
                                inp5_6=int(input("Enter PNR no.(By server):"))
                                amt=df.at[inp5_2,inp5_7]
                                insertrow1=("insert into passenger_detail (pnr_no,username,train_no,from_,to_,class) values(%s,%s,%s,%s,%s,%s);")
                                data1=(inp5_6,inp1,inp5_2,inp5_3,inp5_4,inp5_7,inp5_5)
                                con.execute(insertrow1,data1)
                                cn.commit()
                                print()
                                print("-*"*60)
                                print()
                                print("...............PLEASE WAIT WHILE YOUR TICKET IS BEING GENERATED...................")
                                time.sleep(0.8)
                                print("+"+"-"*128+"+")
                                print("|------Happy Journey!----------------------INDIAN RAILWAY----------------Happy Jorney!----------------|")
                                print("|----------------------------------------------RESERVATION TICKET-----------------------------------------------|")
                                print("+"+"-"*128+"+")
                                print("PNR NO.:",inp5_6,"                         ","Passenger Name.:",inp5_1)
                                print("Phone No.:",inp4,"                  ","Age:",inp5_6)
                                print("GENDER:",gen,"                               ","Date of journey:",yr,"-",mnth,"-",dte)
                                print("Departure Time:",df.at[inp5_2,"DEPARTURE"],"                ","Arrival Time:",df.at[inp5_2,"ARRIVAL"])
                                print("FROM:",inp5_3,"                        ","TO:",inp5_4)
                                print("Class:",inp5_7,"                                  ","Amount:",amt)
                                print("+"+"-"*128+"+")
                                func4()
                            elif inp5==2:
                                print()
                                print("The Train details are:")
                                print("-*"*60)
                                print(df.iloc[0:10,0:4])
                                print()
                                print(df.iloc[0:10,4:7])
                                print()
                                print(df.iloc[0:10,7:11])
                                print()
                                print("-*"*60)
                                print("More routes will be updated soon..")
                                print("-*"*60)
                                func4()
                            elif inp5==3:                        
                                print()
                                issue=str(input("Please give a brief description of the issue you are facing.:"))
                                print()
                                print("-*"*60)
                                print("...Thankyou for your valuable input..." )
                                print()
                                print("...Sorry for inconvenience...")
                                print()
                                print("-*"*60)
                                print("")
                                func4()
                            elif inp5==4:
                                def statistics():
                                    
                                    print()
                                    print("""
                                     +---------------------------------------------------------------------------+
                                     |                              STATISTICS MENU                              |
                                     +---------------------------------------------------------------------------+
                                     |Enter 1:To view statistical data showing time taken by different routes    |
                                     |Enter 2:To view statistical data showing cost variation in class           |
                                     |Enter 3:To view statistical data showing distance covered in each route    |
                                     +---------------------------------------------------------------------------+
                                                   """)
                                    stats=int(input("Please enter any of the given option:"))
                                    if stats==1:
                                        print("The tabular data is given below:")
                                        print()
                                        print(df.loc[:,"HRS"])
                                        print()
                                        print("-*"*60)
                                        print()
                                        print("You can view the graph of the data from Plots pane")
                                        print()
                                        #Line Chart
                                        z2=['12055','12017','14041','12210','12092','15036','15056','22976','5313','12220']
                                        x2=[555,755,2715,11450,824,640,626,2325,625,1542]
                                        plt.plot(z2,x2,'cyan',linestyle='dashed',marker='d',markeredgecolor='red')
                                        plt.xlabel("Train No.")
                                        plt.ylabel("Time taken")
                                        plt.title("Graph showing time taken by different routes")
                                        plt.show()
                                        func4()
                                    elif stats==2:
                                        print("The tabular data is given below:")
                                        print()
                                        print(df.iloc[0:10,6:9])
                                        print()
                                        print("-*"*60)
                                        print()
                                        print("You can view the graph of the data from Plots pane")
                                        print()
                                        #Multiple Bar Chart
                                        plt.figure(figsize=(10,7))
                                        trn1=[750,830,325]
                                        trn2=[745,865,335]
                                        trn3=[1346,1265,560]
                                        trn4=[1390,1315,654]
                                        trn5=[550,730,220]
                                        trn6=[625,780,280]
                                        trn7=[665,795,225]
                                        trn8=[1595,1452,710]
                                        trn9=[665,796,225]
                                        trn10=[935,898,685]
                                        Class=['AC-1','AC-2','Slp']
                                        x=np.arange(len(Class))
                                        plt.bar(Class,trn1,width=0.07,label='train_12055')
                                        plt.bar(x+0.05,trn2,width=0.07,label='train_12017')
                                        plt.bar(x+0.10,trn3,width=0.07,label='train_14041')
                                        plt.bar(x+0.15,trn4,width=0.07,label='train_12210')
                                        plt.bar(x+0.20,trn5,width=0.07,label='train_12092')
                                        plt.bar(x+0.25,trn6,width=0.07,label='train_15036')
                                        plt.bar(x+0.30,trn7,width=0.07,label='train_15056')
                                        plt.bar(x+0.35,trn8,width=0.07,label='train_22976')
                                        plt.bar(x+0.40,trn9,width=0.07,label='train_5313')
                                        plt.bar(x+0.45,trn10,width=0.07,label='train_12220')
                                        plt.legend(loc='upper right')
                                        plt.xlabel("Class")
                                        plt.ylabel("Cost as per different trains")
                                        plt.title("Graph showing cost variation in class")
                                        plt.show()
                                        func4()
                                    elif stats==3:
                                        print("The tabular data is given below:")
                                        print()
                                        print(df.loc[:,"DISTANCE"])
                                        print()
                                        print("-*"*60)
                                        print()
                                        print("You can view the graph of the data from Plots pane")
                                        print()
                                        #Bar Chart
                                        print(df.iloc[0:9,0:3])
                                        x1=['12055','12017','14041','12210','12092','15036','15056','12527','5313','12220']
                                        y2=[315,336,1104,1153,187,237,253,1175,255,783]
                                        plt.bar(x1,y2,color='m')
                                        plt.xlabel("Train No.")
                                        plt.ylabel("Distance")
                                        plt.title("Graph showing distance covered in each route")
                                        plt.show()
                                        func4()
                                    else:
                                        print("Please enter from given options only.")
                                        statistics()
                                statistics()              
                            elif inp5==5:
                                print()
                                log1=str(input("Do you really want to logout? (Y/N)\nEnter Y for yes and N for No:"))
                                print()
                                if log1=="y" or log1=="Y":                             
                                    print("-*"*60)
                                    print("""
                                              ...Thankyou for logging in with us...
                                             """)
                                    print("-*"*60)
                                    func1()
                                elif log1=="n" or log1=="N":
                                    print("-*"*60)
                                    print(("""
                                            ...Thankyou for rejoining with us...
                                         """))
                                    print("-*"*60)
                                    func4()
                            else:                                                    
                                print("!!!Please enter from given options only!!!")
                                print()
                                func3()            
                        func3()
                    else:
                        print("please enter correct password.")
                        func6()
                else:
                    print("please enter correct name")
                    func6()
        func6()
    elif userinput==3:
        func5()
    else:
        print()
        print("!!!Please enter from given options only!!!")
        func1()
#calling function 1
func1()

    

          
        
        
      
            
                    


        
        

              
    
    
    

        
    
    
    
    


