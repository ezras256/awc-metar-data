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

kslg = []

for row in cr:
    for i in range(len(row)):
        if i == 1 and row[i] == 'KSLG':
            kslg = row

metar = kslg[0]

metarDataList = metar.split(' ')

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
tmonth = localdt.month
tyear = localdt.year
thour = localdt.time().hour
tminute = localdt.time().minute

metarData['location'] = loc
metarData['date'] = {'day': tday, 'month': tmonth, 'year': tyear}
metarData['time'] = {'hour': str((int(time[1]) - 5) % 24), 'minute': time[2]}
metarData['report type'] = reportType
metarData['wind'] = wind
print(metarData)
