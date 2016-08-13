
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

print(data)