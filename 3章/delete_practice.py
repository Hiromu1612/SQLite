from my_functions import open_basiccrud_db, close_database

conn,cursor=open_basiccrud_db()
sql="DELETE FROM users WHERE name='山田太郎'"
cursor.execute(sql)
conn.commit()
close_database(conn,cursor)