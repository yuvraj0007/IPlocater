import os
from urllib import request
import json
while True:
    ip =input("Enter the target IP address : ")
    url="http://ip-api.com/json/"
    response = request.urlopen(url+ip)
    data = response.read()
    values = json.loads(data)
    print("IP:"+values['query'])
    print("Status: "+values['status'])
    print("Country: "+values['country'])
    print("Country Code: "+values['countryCode'])
    print("Region: "+values['region'])
    print("Region Name: "+values['regionName'])
    print("city: "+values['city'])
    print("zip: "+values['zip'])
    print("Latitude: "+str(values['lat']))
    print("Longitude: "+str(values['lon']))
    print("Timezone: "+values['timezone'])
    print("ISP: "+values['isp'])
    print("Organization: "+values['org'])
    break
