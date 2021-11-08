import sqlite3
from sqlite3.dbapi2 import DatabaseError
conn=sqlite3.connect('data.sqlite3')
c=conn.cursor()
c.execute('UPDATE account SET PW="1111" WHERE ID="TEST" ')
conn.commit()
conn.close()