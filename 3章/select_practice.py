from my_functions import open_basiccrud_db, close_database
from prettytable import PrettyTable #PrettyTableはターミナル上に整った表を表示するためのライブラリ

conn,cursor=open_basiccrud_db()
sql="SELECT name,age FROM users"
cursor.execute(sql)

result=cursor.fetchall() #fetchall()で全てのデータを取得
table=PrettyTable(["name","age"]) #PrettyTableのインスタンスを作成
for (name,age) in result:
    table.add_row([name,age]) #rowは行
print(table)
close_database(conn,cursor)