import sqlite3
conn=sqlite3.connect('data.sqlite3')
c=conn.cursor()
c.execute("SELECT * FROM account")
data=c.fetchall()
print('帳號\t密碼')
for id,pw in data:
    print(id,pw,sep='\t')
#帳號.....密碼
#TEST    1234
conn.close()