import sqlite3

conn = sqlite3.connect('BOOK.db')
cur=conn.cursor()

#テーブルの作成
sql="CREATE TABLE IF NOT EXISTS books(title TEXT,price INTEGER,arrival_day TEXT)"
cur.execute(sql)

conn.commit()
cur.close()
conn.close()