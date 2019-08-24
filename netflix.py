#!/usr/bin/env python3

'''
Developer : Hamdy Abou El Anein
https://github.com/hamdyaea
http://www.daylightlinux.ch
'''


import json
import http.client

ApiKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Please subscribe to receive your api key

def ListCountry():

    conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
        'x-rapidapi-key': ApiKey
    }

    conn.request("GET", "/aaapi.cgi?t=lc&q=available", headers=headers)

    res = conn.getresponse()
    data = res.read()

    CountryListRaw=data.decode("utf-8")
    #print(CountryListRaw)
    CountryListRawJS=json.loads(CountryListRaw)
    CountryCode=(CountryListRawJS["ITEMS"][0][1])  # OK Works
    print(CountryCode)

ListCountry()
