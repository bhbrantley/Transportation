# Simple script to talk to the WMATA API and
# find out the number of elevators out of service
# on the Green Line today.
#
from __future__ import print_function
import json

from config import demo_api_key

try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request

url = 'https://api.wmata.com/NextBusService.svc/json/jPredictions?StopID=1001498'	

hdrs = {'api_key': demo_api_key} 

Stop_ID = '1001498'
params = {'StopID': Stop_ID}

req = Request(url, headers=hdrs)

response = urlopen(req)
raw_data = response.read()
string_data = raw_data.decode('utf8')
data = json.loads(string_data)

predictions = data['Predictions']

for p in predictions:
    if p['DirectionText'] == "South to Archives":
        time = p['Minutes']
        transit_time = str(time) + " minutes"
        nextbus = "bus in "
    print(nextbus, transit_time)

