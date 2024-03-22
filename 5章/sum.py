import sqlite3

dbpath="csv_test.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT SUM(Fare) FROM titanic"
cursor.execute(sql)

result_sum=cursor.fetchone() #fetchone()で1行取得
print("合計金額:",result_sum[0]) #result_sumはタプルで、タプルの中身は1つだけなので[0]で取り出す

cursor.close()
conn.close()