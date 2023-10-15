import csv
import datetime
import urllib.request
import pytz

localTime = pytz.timezone('US/Central')
metarData = {}
url = 'https://www.aviationweather.gov/adds/dataserver_current/current/metars.cache.csv'
response = urllib.request.urlopen(url)
lines = [line.decode('utf-8') for line in response.readlines()]
cr = csv.reader(lines)

def getMetar(airportName: str) -> str:
    for row in cr:
        for i in range(len(row)):
            if i != 1:
                continue
            else:
                if row[i] != airportName:
                    break
                else:
                    return row[0]

metar = getMetar('KSLG').split(' ')

print(metar)