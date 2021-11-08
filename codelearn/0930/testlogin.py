id = input('請輸入帳號:')
pw = input('請輸入密碼:')

import sqlite3
conn=sqlite3.connect('data.sqlite3')
c=conn.cursor()
# c.execute('SELECT * FROM account WHERE id="{}" AND pw="{}"'.format(id,pw))
c.execute('SELECT * FROM account WHERE id=? AND pw=?',(id,pw))
data = c.fetchall()
if len(data) >0:
    print('登入成功')
else:
    print('登入失敗')