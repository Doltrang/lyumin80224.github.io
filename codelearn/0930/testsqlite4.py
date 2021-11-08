import sqlite3
conn = sqlite3.connect('data.sqlite3')
c = conn.cursor()
c.execute('INSERT INTO account(ID,PW) VALUES("TEST3","3234")')
conn.commit()
conn.close()