__author__ = 'zbnoah2811'

import datetime
netstamp = 1396547090192



def stampToDatetime(netstamp):

    your_timestamp = 1396547090192
    # 1396547090192
    date = datetime.datetime.fromtimestamp(your_timestamp / 1e3)
    # print(datetime.datetime.fromtimestamp(your_timestamp).strftime('%Y-%m-%d %H:%M:%S'))
    print(date)

def datetimeToStamp(dtinput):
    return(int(dtinput.timestamp()))

def in_unix(input):
  start = datetime.datetime(year=1970, month=1, day=1)
  diff = input - start
  return int(diff.total_seconds())

year = 2014
month = 4
day = 10
hour = 7
minute = 0
second = 0

d = datetime.datetime(year,month,day,hour,minute,second)

print(in_unix(d))


