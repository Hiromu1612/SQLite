import sqlite3
from prettytable import PrettyTable

dbpath="csv_test.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

#乗客ID,生存,旅客階級,名前,性別,年齢,兄弟姉妹数,両親子供数,チケット番号,料金,客室,乗船港
sql="CREATE TABLE titanic(PassengerId INTEGER, Survived INTEGER, Pclass INTEGER, Name TEXT,Sex TEXT,Age REAL,SibSp INTEGER,Parch INTEGER,Ticket TEXT,Fare REAL,Cabin TEXT,Embarked TEXT)"

cursor.execute(sql)
conn.commit()

#csvファイルを読み込む
import csv
with open("titanic.csv","r") as f:
    rows=csv.reader(f)
    header=next(rows)
    data=[]
    for row in rows:
        data.append(row) #1行ずつ取り出してdataに追加

#データを登録する
sql="INSERT INTO titanic(PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"

cursor.executemany(sql,data)
conn.commit()

cursor.close()
conn.close()