import _mysql as mysql
import MySQLdb

arr =[]
db = mysql.connect(host="aamboqm7t29sik.csbucglvuwdm.us-east-1.rds.amazonaws.com",user="jross428",
                  passwd="paradyme",db="ebdb")
db.query("""select CONCAT("ALTER TABLE ", TABLE_NAME," CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;") from information_schema.tables where table_schema ="ebdb" and table_type ="BASE TABLE";""")

r=db.store_result()
for i in range(0,r.num_rows()):
    arr.append(r.fetch_row()[0][0].decode('utf-8'))
print(arr)
db = MySQLdb.connect(host="aamboqm7t29sik.csbucglvuwdm.us-east-1.rds.amazonaws.com",user="jross428",passwd="paradyme",db="ebdb")
c=db.cursor()
c.execute("""SET FOREIGN_KEY_CHECKS = 0;""")
for cmd in arr:
    c.execute(cmd)
c.execute("""SET FOREIGN_KEY_CHECKS = 1;""")
