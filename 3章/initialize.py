import sqlite3
#データベースとの接続
dbpath="3章/basic_crud.db"
conn=sqlite3.connect(dbpath)
#カーソルの取得
cursor=conn.cursor()
sql="CREATE TABLE IF NOT EXISTS users(name TEXT,age INTEGER,dateofbirth TEXT,sex TEXT,email TEXT)"
#sqlの実行
cursor.execute(sql)
#データベースへ反映
conn.commit()
cursor.close()
conn.close()