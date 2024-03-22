import sqlite3

dbpath="csv_test.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT COUNT(*) FROM titanic WHERE Age <>''" #Ageが空白でないものを対象にする

cursor.execute(sql)

result_count=cursor.fetchone() #fetchone()で1行取得
print(result_count[0]) #result_countはタプルで、タプルの中身は1つだけなので[0]で取り出す

cursor.close()
conn.close()