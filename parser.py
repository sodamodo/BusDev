
import requests
import time
import csv
import yaml
import psycopg2
import datetime
conn_string = "host='localhost' dbname='bus' user='postgres' password='geografio'"
# conn_string = "host='168.62.176.216' dbname='bus' user='postgres' password='altsam'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

writer=csv.writer(open('uberdata.csv','wb'))


year = 2014
month = 3
day = 4
hour = 7
minute = 0
second = 0



def make_link(time):
    link = "http://216.27.87.29/athens/packet/json/vehicle?routes=581,582,598,583,599,584,585,586,587,588,589,590,591,592,593,594,595,596,597&lastVehicleHttpRequestTime=%s" % time
    return link

def get_data(link):
    req = requests.get(link)
    data = yaml.load(req.text)
    return data

def in_unix(input):
  start = datetime.datetime(year=1970, month=1, day=1)
  diff = input - start
  return int(diff.total_seconds())

def floater(loc):
    return float(loc)/100000

def data_strip(data):

    stripped = data['VehicleArray']
    row = []
    for i in range(len(stripped)):
        subrow = []
        subrow.append(stripped[i]['vehicle']['CVLocation']['locTime'])
        subrow.append(stripped[i]['vehicle']['routeID'])
        subrow.append(stripped[i]['vehicle']['CVLocation']['speed'])
        subrow.append(floater(stripped[i]['vehicle']['CVLocation']['latitude']))
        subrow.append(floater(stripped[i]['vehicle']['CVLocation']['longitude']))
        row.append(subrow)
    return row




def query(daystart,dayend):
    grandarray = []
    for day in range(daystart, dayend):
        print("day %s" % day)
        for hour in range(6, 23):
            print("hour %s" % hour)
            for minute in range(1, 60):
                for second in range(0, 60, 30):
                    d = datetime.datetime(year, month, day, hour, minute, second)
                    grandarray = data_strip(get_data(make_link(in_unix(d))))
                    for rows in grandarray:
                        writer.writerow([datetime.datetime.fromtimestamp(rows[0]).strftime('%Y-%m-%d %H:%M:%S'), rows[1], rows[2],rows[3],rows[4]])

    # return grandarray


# def processor(grandarray):
#
#     for rows in grandarray:
#         for subrows in rows:
#             tupe = (subrows[0], subrows[1], subrows[2], subrows[3], subrows[4])
#             cursor.execute("""INSERT INTO bus (time,route,speed,latitude,longitude) VALUES (%s,%s,%s,%s,%s);""", tupe)
#             conn.commit()
#
#
#     valuelist = []
#     cursor.execute("SELECT * FROM bus")
#     records = cursor.fetchall()
#     count = 0
#     for i in records:
#          valuelist.append(((datetime.datetime.fromtimestamp(i[0]).strftime('%Y-%m-%d %H:%M:%S')), i[1], i[2],i[3],i[4]))
#          count += 1
#          if count % 100 == 0:
#              print count
#
#     count = 0
#     for r in valuelist:
#          # cursor.execute("""INSERT INTO rebus (time,route,speed,latitude,longitude) VALUES (%s,%s,%s,%s,%s);""", r)
#          # conn.commit()
#          writer.writerow(r)
#          count += 1
#          if count % 100 == 0:
#              print count
#



query(1,3)



