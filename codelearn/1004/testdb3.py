import dataset
import pymysql
pymysql.install_as_MySQLdb()

db = dataset.connect('mysql://root:Tcfst123456!@localhost:3306/cmdev')
print(list(db['emp']))