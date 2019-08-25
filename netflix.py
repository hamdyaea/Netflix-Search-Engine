#!/usr/bin/env python3

'''
Developer : Hamdy Abou El Anein
https://github.com/hamdyaea
http://www.daylightlinux.ch
'''

from easygui import *
import json
import http.client

netflixLogo = "/pictures/netflix.gif"

ApiKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Please subscribe to receive your api key

def ListCountry():
    global CountryShortCode

    countries="Argentina","Belgium","Brazil","Canada","Czech Republic","France","Germany","Greece","Hong Kong","Iceland","India", \
    "Israel","Italy","Japan","Lithuania","Mexico","Netherlands","Poland","Portugal","Romania","Russia","Singapore", \
    "Slovakia","South Africa","South Korea","Spain","Sweden","Switzerland","Thailand","United Kingdom","United States"
    CountrySelect = choicebox(msg='Pick something.', title='Netlfix', choices=(countries))
    if CountrySelect == "Argentina":
         CountryShortCode="ar"
    elif CountrySelect =="Belgium":
         CountryShortCode="be"
    elif CountrySelect == "Brazil":
         CountryShortCode = "br"
    elif CountrySelect == "Canada":
         CountryShortCode = "ca"
    elif CountrySelect == "Czech Republic":
         CountryShortCode = "cz"
    elif CountrySelect == "France":
         CountryShortCode = "fr"
    elif CountrySelect == "Germany":
         CountryShortCode = "de"
    elif CountrySelect == "Greece":
         CountryShortCode = "gr"
    elif CountrySelect == "Hong Kong":
         CountryShortCode = "hk"
    elif CountrySelect == "Iceland":
         CountryShortCode = "is"
    elif CountrySelect == "India":
         CountryShortCode = "in"
    elif CountrySelect == "Israel":
         CountryShortCode = "il"
    elif CountrySelect == "Italy":
         CountryShortCode = "it"
    elif CountrySelect == "Japan":
         CountryShortCode = "jp"
    elif CountrySelect == "Lithuania":
         CountryShortCode = "lt"
    elif CountrySelect == "Mexico":
         CountryShortCode = "mx"
    elif CountrySelect == "Netherlands":
         CountryShortCode = "nl"
    elif CountrySelect == "Poland":
         CountryShortCode = "pl"
    elif CountrySelect == "Portugal":
         CountryShortCode = "pt"
    elif CountrySelect == "Romania":
         CountryShortCode = "ro"
    elif CountrySelect == "Russia":
         CountryShortCode = "ru"
    elif CountrySelect == "Singapore":
         CountryShortCode = "sg"
    elif CountrySelect == "Slovakia":
         CountryShortCode = "sk"
    elif CountrySelect == "South Africa":
         CountryShortCode = "za"
    elif CountrySelect == "South Korea":
         CountryShortCode = "kr"
    elif CountrySelect == "Spain":
         CountryShortCode = "es"
    elif CountrySelect == "Sweden":
         CountryShortCode = "se"
    elif CountrySelect == "Switzerland":
         CountryShortCode = "ch"
    elif CountrySelect == "Thailand":
         CountryShortCode = "th"
    elif CountrySelect == "United Kingdom":
         CountryShortCode = "gb"
    elif CountrySelect == "United States":
         CountryShortCode = "us"
    print(CountryShortCode)

def Last7daysNews():
    conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
        'x-rapidapi-key': ApiKey
    }

    conn.request("GET", "/aaapi.cgi?q=get%3Anew7%3A"+str(CountryShortCode)+str("&p=1&t=ns&st=adv"), headers=headers)

    res = conn.getresponse()
    data = res.read()

    ListNewRaw=(data.decode("utf-8"))
    ListNewJson=json.loads(ListNewRaw)
    New7Movies = ""

    key = int(ListNewJson["COUNT"])

    count = 0
    while count <= key-1:
        New7Movies = New7Movies + (ListNewJson["ITEMS"][count]["title"])+str("\n")
        count = count + 1
        if count > key-1:
            break

    print(New7Movies)

ListCountry()
Last7daysNews()