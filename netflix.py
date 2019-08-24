#!/usr/bin/env python3

'''
Developer : Hamdy Abou El Anein
https://github.com/hamdyaea
http://www.daylightlinux.ch
'''



import requests

ApiKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Please subscribe to receive your api key

def ListCountry():

    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"t":"lc","q":"available"}

    headers = {
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",  # Please subscribe to receive your api key
        'x-rapidapi-key': ApiKey
        }

    response = requests.request("GET", url, headers=headers, params=querystring,file=open("output.txt", "a"))

    print(response.text)

ListCountry()
