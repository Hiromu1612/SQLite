import sqlite3

dbpath="firstdb.db"
conn = sqlite3.connect(dbpath)
conn.close()
