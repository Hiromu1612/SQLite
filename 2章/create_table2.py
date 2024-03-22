import sqlite3

#データベースとの接続
dbpath="firstdb.db"
conn = sqlite3.connect(dbpath)
#カーソルの取得
cursor= conn.cursor()
#テーブルの作成 カラム名 データ型 制約
sql="CREATE TABLE IF NOT EXISTS users2(name TEXT PRIMARY KEY,age INTEGER,dateofbirth TEXT,sex TEXT,email TEXT NOT NULL)"
#SQLの実行
cursor.execute(sql)
#データベースへ反映
conn.commit()
#カーソルを閉じる
cursor.close()
#データベースとの接続を切断
conn.close()