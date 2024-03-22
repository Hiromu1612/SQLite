import sqlite3

#データベースとの接続
dbpath="firstdb.db"
conn = sqlite3.connect(dbpath)
#カーソルの取得
cursor= conn.cursor()
#カラムの追加 カラム名 データ型 制約
sql="ALTER TABLE users3 ADD COLUMN phone INTEGER"
#SQLの実行
cursor.execute(sql)
#データベースへ反映
conn.commit()
#カーソルを閉じる
cursor.close()
#データベースとの接続を切断
conn.close()