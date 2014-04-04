__author__ = 'zbnoah2811'

import datetime
your_timestamp = 1396547090192
# 1396547090192
date = datetime.datetime.fromtimestamp(your_timestamp / 1e3)
# print(datetime.datetime.fromtimestamp(your_timestamp).strftime('%Y-%m-%d %H:%M:%S'))
print date