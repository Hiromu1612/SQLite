import sqlite3
from prettytable import PrettyTable

dbpath="csv_test.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT Embarked FROM titanic GROUP BY Embarked" #重複を除いた値を取得
cursor.execute(sql)
result=cursor.fetchall()
table=PrettyTable(["Embarked"])
for (Embarked) in result:
    table.add_row([Embarked])
print(table)

sql="SELECT Embarked,COUNT(*) FROM titanic GROUP BY Embarked"
cursor.execute(sql)
result=cursor.fetchall()
table=PrettyTable(["Embarked","Count"])
for (Embarked,Count) in result:
    table.add_row([Embarked,Count])
print(table)

cursor.close()
conn.close()