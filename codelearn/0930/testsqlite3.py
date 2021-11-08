import sqlite3
conn = sqlite3.connect('data.sqlite3')
c = conn.cursor()
c.execute('''
    create table account(
        ID text,
        PW text
    )
''')
conn.close()