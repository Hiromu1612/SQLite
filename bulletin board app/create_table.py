import sqlite3

conn=sqlite3.connect('Books.db')
cur=conn.cursor()

#テーブルの作成
sql="CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT,  name TEXT,  author TEXT,  evaluation TEXT,  status TEXT,  purchase_date TEXT,  start_date TEXT,   end_date TEXT,  pages INTEGER,   url TEXT,   comment TEXT)"
cur.execute(sql)

#データの挿入
sql="INSERT INTO books(name,author,evaluation,status,purchase_date,start_date,end_date,pages,url,comment) VALUES(?,?,?,?,?,?,?,?,?,?)"
cur.execute(sql,("Python実践入門","小川雄太郎","A","読了","2021/12/10","2021/12/11","2021/12/12",300,"https://www.google.com","Pythonの実践的な使い方を学ぶ"))

conn.commit()
cur.close()
conn.close()