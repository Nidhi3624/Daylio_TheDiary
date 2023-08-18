import datetime
import pickle
tdate=datetime.date.today()

xy=open("f:\\reminderss.csv","a+")
xy.close()

def todo():
    global tdate
    k=[]
    m=1
    n=0
    while n==0:
        z=input("Enter a task:")
        w=str(tdate)
        t=[w,m,z]
        k.append(t)
        m=m+1
        ch=input("Do you want to enter more tasks? Yes/no:")
        if ch in ["No","no"]:
            n=1
            
    import csv
    f=open("f:\\todo-list.csv","a+")
    v=csv.writer(f)
    v.writerows(k)
    f.close()

def todaystask():
    import csv
    v=str(input("Enter date to display it's to-do list:"))
    global tdate
    fl=open("f:\\todo-list.csv","r")
    rd=csv.reader(fl)
    print("Today's tasks are:") 
    for r in rd:
        for j in r:
            if j==v:
                print(r[1]+".",r[2])
    fl.close()

def todaysreminders():
    import csv
    global tdate
    fl=open("f:\\reminderss.csv","r")
    rd=csv.reader(fl)
    print("today's reminders are:")
    for i in rd:
        for j in i:
            if j==str(tdate):
                print(i[1])
    fl.close()

def reminder():
    l=[]
    choice="yes"
    while choice=="yes":
        rdate=str(input("Please enter the date(YYYY-MM-DD) of reminder:"))
        print("Please enter the reminder")
        remind=str(input("Remind me to:"))
        a=[rdate,remind]
        l.append(a)
        choice=input("Would you like to set more reminders? yes/no?")
        
    import csv
    f=open("f:\\reminderss.csv","a+")
    w=csv.writer(f)
    w.writerows(l)
    f.close()

def thought():
    import random
    thoughts=["'Believe you can and you are halfway there!'","'You must be the change you wish to see in the world!'","'Everyday is a chance to be better!'","'Don't wish for it, work for it!'","'Work hard in silence and let success make the noise!'","'You are the artist of your own life!'"]
    x=random.randrange(0,6)
    print("Today's quote:")
    print( thoughts[x])

def write():
    global tdate
    name=str(tdate)
    f=open("f:\\diaryenteriess\\"+name+".dat","wb")
    l=str(input("Dear Diary,"))
    pickle.dump(l,f)
    f.close()
    
def read():
    try:
        date=str(input("enter the date to read diary entry:"))
        g=open("f:\\diaryenteriess\\"+date+".dat","rb")
        print(date)
        try:
            while True:
                x=pickle.load(g)
                print(x)
        except EOFError:
            g.close()
    except FileNotFoundError:
        print("There's no diary entry on this date...")
    
    
def update():
    date=str(input("enter the date to update its diary entry:"))
    u=open("f:\\diaryenteriess\\"+date+".dat","ab")
    x=input("start writing:")
    pickle.dump(x,u)
    u.close()

     
print("---------------------------------------------------------------------------------------------------------------------")
print("***************************************** DAYLIO: THE DIARY ***************************************************************")
print("---------------------------------------------------------------------------------------------------------------------")

print ("Hello, Welcome back!")
print( )
print("_____________________________________________________________________________________________________________________")
print( )
thought()
print( )
print("---------------------------------------------------------------------------------------------------------------------")
print( )
todaysreminders()
print( )
print("---------------------------------------------------------------------------------------------------------------------")
print( )
print("Here's what you can do in this application.")
print( )
print("1. write=Press 1 to write today's diary entry")
print("2. update=Press 2 to update an entry")
print("3. read=Press 3 to read an entry")
print("4. remind=Press 4 to set a reminder")
print("5. makelist=Press 5 to make a to-do list")
print("6. to-dolist=Press 6 to display your to-do list")
print( )
print("---------------------------------------------------------------------------------------------------------------------")
print( )
choice="yes"
while choice=="yes":
    x=int(input("what would you like to do today?"))
    if x==1:
        write()
        print( )
        choice=input("Would u like to try something else? yes/no")
        print( )
    elif x==3:
        read()
        print( )
        choice=input("Would u like to try something else? yes/no")
        print( )
    elif x==2:
        update()
        print( )
        choice=input("Would u like to try something else? yes/no")
        print( )
    elif x==4:
        reminder()
        print( )
        choice=input("Would u like to try something else? yes/no")
        print( )
    elif x==5:
        todo()
        print( )
        choice=input("Would u like to try something else? yes/no")
        print( )
    elif x==6:
        todaystask()
        print( )
        choice=input("Would u like to try something else? yes/no")
        print( )
    else:
        print("Thank you for visiting! :)")
    print( )
    print("_________________________________________________________________________________________________________________")
    print( )
print("Thank you for visiting! :)")
print("_________________________________________________________________________________________________________________")
