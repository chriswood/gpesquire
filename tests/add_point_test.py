import urllib2
import json

jdata = json.dumps({"latitude":"36.123456", "longitude":"-86.345345"})
response = urllib2.urlopen("http://127.0.0.1:8000/add_point/", jdata)
print(response)
print("done")
