import sqlite3
from prettytable import PrettyTable

dbpath="csv_test.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT Embarked,COUNT(*),ROUND(AVG(Fare),2),SUM(Fare) FROM titanic GROUP BY Embarked" 
cursor.execute(sql)
result=cursor.fetchall()
table=PrettyTable(["Embarked","Count","Average","Sum"])
for (Embarked,Count,Average,Sum) in result:
    table.add_row([Embarked,Count,Average,Sum])
print(table)

cursor.close()
conn.close()