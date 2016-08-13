
#	simple script to talk to the WMATA API

import json

try:
	from urllib2 import urlopen, Request
except ImportError:
	from urllib.request import urlopen, Request

demo_api_key = '6b700f7ea9db408e9745c207da7ca827'
url = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'
headers = {
    # Request headers
    'api_key': demo_api_key,
}
req = Request(url, headers=headers)
response = urlopen(req)

raw_data = response.read()
string_data = raw_data.decode('utf8')
data = json.loads(string_data)

incidents = data['ElevatorIncidents']
first_incident = incidents[0]


stations_url = 'https://api.wmata.com/Rail.svc/json/jStations[?LineCode]'
req2 = Request(stations_url, headers=headers)
response2 = urlopen(req2)
stations_data = json.loads(response2.read().decode('utf8'))
station_codes = []
stations_list = stations_data['Stations']
for s in stations_list:
	station_code = s['Code']
	station_codes.append(station_code)

for i in incidents:
	station_code = i['StationCode']
	if station_code in station_codes and i['UniteType'] == 'ELEVATOR':
		description = i['LocationDescription']
		print(description)
