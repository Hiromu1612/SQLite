import sqlite3
from prettytable import PrettyTable

dbpath="csv_test.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT * FROM titanic ORDER BY Pclass LIMIT 40 OFFSET 300" #OFFSETで指定した行数だけスキップ
cursor.execute(sql)
result=cursor.fetchall()
table=PrettyTable(["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"])
for (PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked) in result:
    table.add_row([PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked])
print(table)

cursor.close()
conn.close()