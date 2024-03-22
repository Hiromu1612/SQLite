from my_functions import open_basiccrud_db, close_database

conn,cursor=open_basiccrud_db()
sql="CREATE TABLE IF NOT EXISTS users2(name TEXT,age INTEGER,dateofbirth TEXT,sex TEXT,email TEXT)"
cursor.execute(sql)
conn.commit()
close_database(conn,cursor)