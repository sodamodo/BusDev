import psycopg2
import datetime


conn_string = "host='168.62.176.216' dbname='bus' user='postgres' password='altsam'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()




cursor.execute("SELECT * FROM bus;")

valuelist = []
records = cursor.fetchall()
count = 0
for i in records:
     valuelist.append(((datetime.datetime.fromtimestamp(i[0]).strftime('%Y-%m-%d %H:%M:%S')), i[1], i[2],i[3],i[4]))
     count += 1
     if count % 100 == 0:
         print count

count = 0
for r in valuelist:
     cursor.execute("""INSERT INTO rebus (time,route,speed,latitude,longitude) VALUES (%s,%s,%s,%s,%s);""", r)
     conn.commit()
     count += 1
     if count % 100 == 0:
         print count



cursor.execute("SELECT * FROM rebus LIMIT 1000")
print cursor.fetchall()




# values = ((datetime.datetime.fromtimestamp(records[0]).strftime('%Y-%m-%d %H:%M:%S')), records[1], records[2],records[3],records[4])
# print values
# # insert = "INSERT into rebus (time,route,speed,latitude,longitude) VALUES (%s,%s,%s,%s,%s)", records
# for i in range(10):
#     cursor.execute("""INSERT INTO rebus (time,route,speed,latitude,longitude) VALUES (%s,%s,%s,%s,%s);""", values)

