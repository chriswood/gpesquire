import urllib2
import json

# pushing button causes something like this to run...
#raw_data = gps_poller.get_data()

# build django serialized object type json
#dso = {'fields': {'plan_id': 1, 'lat': '36.123456', 'lon':'-86.345345', 'meters_error': 3}}
dso = {'plan_id': 1, 'lat': '45.123456', 'lon':'-86.345345', 'meters_error': 3}
jdata = json.dumps(dso)
response = urllib2.urlopen("http://127.0.0.1:8000/add_point/", jdata)
print(response)
print("done")
