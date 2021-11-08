import sqlite3
from sqlite3.dbapi2 import DatabaseError
conn=sqlite3.connect('data.sqlite3')
c=conn.cursor()
c.execute('DELETE FROM account WHERE ID="TEST3" ')
conn.commit()
conn.close()