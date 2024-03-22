import sqlite3
from prettytable import PrettyTable

dbpath="basic_crud.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT * FROM users WHERE dateofbirth like '197_%'" #LIKEは部分一致 %は任意の文字列 _は任意の一文字
cursor.execute(sql)

result=cursor.fetchall()
table=PrettyTable(["name","age","dateofbirth","sex","email"])
for (name,age,dateofbirth,sex,email) in result:
    table.add_row([name,age,dateofbirth,sex,email])
print(table)

cursor.close()
conn.close()