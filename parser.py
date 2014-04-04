
import requests
import time
import csv
import yaml
import psycopg2

now = int((time.time()))
staticnow = 1393063058901
dayend = 1396299619
minute = 60
hour = 3600
day = hour * 24
week = day * 7
daycount = 10
now = int((time.time()))

def make_link(time):
    link = "http://216.27.87.29/athens/packet/json/vehicle?routes=581,582,598,583,599,584,585,586,587,588,589,590,591,592,593,594,595,596,597&lastVehicleHttpRequestTime=%s" % time
    return link

def get_data(link):
    req = requests.get(link)
    data = yaml.load(req.text)
    return data

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



def floater(loc):
    return float(loc)/100000


writer=csv.writer(open('data','wb'))

for i in range(60,day,60):
    time = now - i
    nestrow = data_strip(get_data(make_link(time)))
    for row in nestrow:
        writer.writerow(row)





