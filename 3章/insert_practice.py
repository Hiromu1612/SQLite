from my_functions import open_basiccrud_db, close_database

conn,cursor=open_basiccrud_db()
sql="INSERT INTO users(name,age,dateofbirth,sex,email) VALUES('Miura Naoya',47,'1975/5/8','M','miura@gmail.com')"
cursor.execute(sql)
conn.commit()
close_database(conn,cursor)