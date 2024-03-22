from my_functions import open_basiccrud_db, close_database

conn,cursor=open_basiccrud_db()
params = [
    ('Nakamura Hideyuki', 65, '1957/5/13', 'M', 'hideyuki_nakamura_25908461@hotmaill.com'),
    ('Sugino Miyoko', 50, '1972/5/7', 'F', 'miyokosugino_79572062@gmail.com'),
    ('Noda Yurika', 40, '1982/1/16', 'F', 'yurikanoda_05497229@hotmaill.com')
]
sql="INSERT INTO users VALUES (?,?,?,?,?)" #valuesの?はプレースホルダ プレースホルダは後で値を埋めるためのもの

#服すレコードの作成はexecutemany()メソッドを使う
cursor.executemany(sql,params)
conn.commit()
close_database(conn,cursor)