import mysql.connector

cnx = mysql.connector.connect(user='root', password='Tcfst123456!',
                              host='127.0.0.1',
                              database='cmdev')
c = cnx.cursor()
c.execute('SELECT * FROM emp')
# print(c.fetchall())
data=c.fetchall()
print(data)
print('-----------')
for row in data:
    print(row[0],row[1],row[2],sep='\t')
cnx.close()