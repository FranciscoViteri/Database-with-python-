import sqlite3
from sqlite3 import Error
import random
import datetime

import time

try:
    # Database IN MEMORY 
    #db = sqlite3.connect(':memory:')

    #Database on DISK
    db = sqlite3.connect('test.db')
except Error as e:
    print(e)
finally:
    cur=db.cursor()
    createtable = "create table sales(saledate date, item integer, total float)"
    cur.execute(createtable)
    start1 = datetime.datetime.now()
    for x in range(0, 100000):
        xitem = random.randint(1,100)
        xtotal = round(random.uniform(50,90), 4)
        pastdays = datetime.timedelta(days=365)
        lastyear = datetime.date.today() - pastdays
        start_date = lastyear.replace(day=1, month=1).toordinal()
        
        end_date = datetime.date.today().toordinal()
        random_day = datetime.date.fromordinal(random.randint(start_date, end_date))
        xdate=random_day
        
        cur.execute('insert into sales (saledate, item, total) values (?,?,?)',(xdate,xitem,xtotal))
        
    end1 = datetime.datetime.now()     
    start2 = datetime.datetime.now()     
    rows = cur.execute('select * from sales order by item, saledate')
    end2 = datetime.datetime.now()
    start3 = datetime.datetime.now()
    for row in rows:
        print(row)
    end3 = datetime.datetime.now()
    db.commit()
    db.close()
    print('Insert process took: ',end1-start1)
    print('Query process  took: ',end2-start2)
    print('Display result took: ',end3-start3)
