import sqlite3
from datetime import datetime

name=sqlite3.connect("money management.db")
cursor=name.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS money_management(
your_balance  INTEGER,
reason  TEXT NOT NULL,
date    INTEGER)
"""
)

now=datetime.now()
date=now.date()

print("welcome in your money management app")
message=("""enter what do want to do 
      1-show you balance
      2-add-money
      3-decreace money
      4-show reacons
      5-exit program
      choose from(1,2,3,4,5)""")

sum=cursor.execute("SELECT SUM(your_balance) FROM money_management")
total=cursor.fetchone()[0]

def commet_and_close():
    name.commit()
    name.close()

def show():
        try:
            if total > 0:
                print(f"your money is equal {total}")
            elif total==0:
                print("your amount is equal zero😑")
        except:
            print("you have a empty data base")
def add():
    new=input("enter amount you want to add:").strip()
    reason=input("enter how you gain this money:").strip().capitalize()
    cursor.execute(F"INSERT INTO money_management(your_balance,reason,date) VALUES('{new}','{reason}','{date}')")
    print("money was added😑")

def decrease():

    num=int(input("enter the number you want to deacreace it:"))
    reason=input("enter a reason you spend money on it:")
    if num>0:
        num=-num
        result=total+num
        print(f"the total became equal {result}")
        cursor.execute(f"INSERT INTO money_management(your_balance,reason,date) VALUES('{result}','{reason}','{date}')")
    elif num<0:
        result=total+num
        print(f"the total become equal {result}")
        cursor.execute(f"INSERT INTO money_management(your_balance,reason,date) VALUES('{result}','{reason}','{date}')")
    else:
        print("you have a error in you input")
        
def reason():
    cursor.execute("select * from money_management")
    result=cursor.fetchall()
    x=1
    for row in result:
        print(f"{x}-{row[1]}")
        x=x+1

def close():
    commet_and_close()

while True:
    choose=int(input(message))
    if choose==1:
        show()
    
    elif choose==2:
        add()
        commet_and_close()
    
    elif choose==3:
        decrease()
    
    elif choose==4:
        reason()

    elif choose==5:
        commet_and_close()
        break

    else:
        print("you have an input error.")
    

