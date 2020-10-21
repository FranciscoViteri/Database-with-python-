import sqlite3
import csv

db = sqlite3.connect('cameras.db')
cursor = db.cursor()
rows = cursor.execute("select camera,count(*) as Hits,strftime('%d',logdate), strftime('%H',logtime) as Day from log1 group by 1,3,4")
csv_file = csv.writer(open("my_file.csv","w"))
csv_file.writerow(['camera','Day','Hour'])
for row in rows:
    csv_file.writerow(row)
    print(row)

