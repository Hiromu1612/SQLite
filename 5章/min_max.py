import sqlite3

dbpath="csv_test.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT MIN(Fare) FROM titanic"
cursor.execute(sql)
min=cursor.fetchone()
print(min[0])

sql="SELECT MAX(Fare) FROM titanic"
cursor.execute(sql)
max=cursor.fetchone()
print(max[0])

cursor.close()
conn.close()