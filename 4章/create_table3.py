import sqlite3

#データベースとの接続
dbpath="basic_crud.db"
conn = sqlite3.connect(dbpath)

cursor= conn.cursor()#カーソルの取得

#テーブルの作成 カラム名 データ型 制約
sql="CREATE TABLE IF NOT EXISTS invoices(id INTEGER PRIMARY KEY, name TEXT,date TEXT, total INTEGER)"
cursor.execute(sql)#SQLの実行
conn.commit()#データベースへ反映


params = [
    ('Miura Naoya', '2022/5/8', '580'),
    ('Noda Yurika', '2022/5/8', '580'),
    ('Noda Yurika', '2022/5/30', '5250'),
    ('Noda Yurika', '2022/6/18', '2500'),
    ('Noda Yurika', '2022/6/29', '880'),
    ('Miura Naoya', '2022/6/30', '1160'),
]
sql="INSERT INTO invoices(name,date,total) VALUES (?,?,?)" #?はプレースホルダ
cursor.executemany(sql, params)
conn.commit()


cursor.close()
conn.close()