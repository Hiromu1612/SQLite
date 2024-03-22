import sqlite3
from prettytable import PrettyTable

dbpath="csv_test.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT Embarked,COUNT(*) FROM titanic WHERE Sex='female' GROUP BY Embarked HAVING COUNT(*)>50 "
cursor.execute(sql)
result=cursor.fetchall()
table=PrettyTable(["Embarked","Count"])
for (Embarked,Count) in result:
    table.add_row([Embarked,Count])
print(table)

cursor.close()
conn.close()