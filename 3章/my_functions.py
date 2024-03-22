import sqlite3
def open_basiccrud_db():
    #データベースとの接続
    conn=sqlite3.connect("basic_crud.db")
    #カーソルの取得
    cursor=conn.cursor()
    return conn,cursor

def close_database(conn,cursor):
    cursor.close()
    conn.close()