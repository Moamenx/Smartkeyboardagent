from _datetime import datetime
import MySQLdb
import time

dict ={}
db = MySQLdb.connect("localhost","root","root","test")

cursor = db.cursor()
user_ids =[]

ids_query = 'SELECT distinct user_id FROM typedwords'
cursor.execute(ids_query)
ids = cursor.fetchall()
for id in ids:
    dict[id[0]] = []
    user_ids.append(id[0])

for id in user_ids:
    query = "SELECT sentence FROM typedwords WHERE date>= NOW() - INTERVAL 1 DAY AND user_id= '{id}';".format(id=id)

    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        dict[id].append(row[0])

#query = "SELECT id, sentence FROM typedwords WHERE date>= NOW() - INTERVAL 1 DAY;"
#time =time.strftime("%Y-%m-%d %H:%M:%S")
# #query = sql = "SELECT * FROM api_typedwords WHERE INCOME > '%d'" % (1000)
# sql =  "INSERT INTO typedwords VALUES(%s, %s, %s,%s)"
# values = (6, 'football is nice', time, 3)
# cursor.execute(sql, values)
# db.commit()
#cursor.execute(query)
#result = cursor.fetchall()
#for row in result:
#    print(row[0])
#    print(row[1])
#    print('-------------------')
db.close()

print(dict)