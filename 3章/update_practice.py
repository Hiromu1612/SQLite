from my_functions import open_basiccrud_db, close_database

conn,cursor=open_basiccrud_db()
sql="UPDATE users SET age=20"
cursor.execute(sql)
conn.commit()
close_database(conn,cursor)