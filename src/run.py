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

airportData = []

for row in cr:
    for i in range(len(row)):
        if i == 1:
            if row[i] == 'KSLG':
                airportData = row
            elif row[i] == 'KXNA':
                airportData = row
print(airportData)

metar = airportData[0]

metarDataList = metar.split(' ')
print(metarDataList)
for i in metarDataList:
    if i == 'AUTO':
        metarDataList.pop(metarDataList.index(i))
    # if i == 'RMK':
        # for j in range(len(metarDataList) - metarDataList.index(i)):
            # ind = metarDataList.index(i) + j
            # 

print(metarDataList)

loc = metarDataList[0]
time = [
    metarDataList[1][0:2], metarDataList[1][2:4], metarDataList[1][4:6],
    metarDataList[1][6]
]
reportType = metarDataList[2]
wind = [metarDataList[3][0:3], metarDataList[3][3:5], metarDataList[3][5:8]]
print(metarDataList)
dt = datetime.datetime.now()
localdt = dt.replace(tzinfo=pytz.utc).astimezone(localTime)
tday = localdt.day
thour = localdt.time().hour
tminute = localdt.time().minute

metarData['location'] = loc
metarData['day'] = tday
metarData['time'] = [(int(time[1]) - 5) % 24, time[2]]
metarData['report type'] = reportType
metarData['wind'] = wind
print(metarData)
