from my_functions import open_basiccrud_db, close_database
from prettytable import PrettyTable

conn,cursor=open_basiccrud_db()
sql="SELECT * FROM users"
cursor.execute(sql)
result=cursor.fetchall()
table=PrettyTable(["name","age","dateofbirth","sex","email"])
for (name,age,dateofbirth,sex,email) in result:
    table.add_row([name,age,dateofbirth,sex,email])
print(table)
close_database(conn,cursor)