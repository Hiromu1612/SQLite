import sqlite3
from prettytable import PrettyTable

dbpath="basic_crud.db"
conn=sqlite3.connect(dbpath)
cursor=conn.cursor()

sql="SELECT * FROM users WHERE age IN(40,47)" #INはいずれかの値に一致
cursor.execute(sql)

result=cursor.fetchall()
table=PrettyTable(["name","age","dateofbirth","sex","email"])
for (name,age,dateofbirth,sex,email) in result:
    table.add_row([name,age,dateofbirth,sex,email])
print(table)

cursor.close()
conn.close()