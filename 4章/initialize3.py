import sqlite3

#データベースとの接続
dbpath="basic_crud.db"
conn = sqlite3.connect(dbpath)

cursor= conn.cursor()#カーソルの取得

params = [
    ('Miura Naoya', 47, '1975/5/8', 'M', 'miura_naoya_91689485@gmail.com'),
    ('Nakamura Hideyuki', 65, '1957/5/13', 'M', 'hideyuki_nakamura_25908461@hotmaill.com'),
    ('Sugino Miyoko', 50, '1972/5/7', 'F', 'miyokosugino_79572062@gmail.com'),
    ('Noda Yurika', 40, '1982/1/16', 'F', 'yurikanoda_05497229@hotmaill.com')
]
sql = "INSERT INTO users (name,age,dateofbirth,sex,email) VALUES (?,?,?,?,?)" #?はプレースホルダ
cursor.executemany(sql, params)
conn.commit()

cursor.close()
conn.close()