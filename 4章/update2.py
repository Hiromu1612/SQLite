import sqlite3
from prettytable import PrettyTable

dbpath="basic_crud.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="UPDATE users SET age=?, dateofbirth=? WHERE name=?"

params=[48, "1974/5/8","Miura Naoya"]
cursor.execute(sql,params)
conn.commit()
conn.close()