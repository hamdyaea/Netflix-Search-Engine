#!/usr/bin/env python3

'''
Developer : Hamdy Abou El Anein
https://github.com/hamdyaea
http://www.daylightlinux.ch
'''

import sys
from easygui import *
import json
import http.client

netflixLogo = "./pictures/netflix.gif"

ApiKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Please subscribe to receive your api key

def ListCountry():
    global CountryShortCode,CountrySelect

    countries="Argentina","Belgium","Brazil","Canada","Czech Republic","France","Germany","Greece","Hong Kong","Iceland","India", \
    "Israel","Italy","Japan","Lithuania","Mexico","Netherlands","Poland","Portugal","Romania","Russia","Singapore", \
    "Slovakia","South Africa","South Korea","Spain","Sweden","Switzerland","Thailand","United Kingdom","United States"
    CountrySelect = choicebox(msg='Select your country', title='Netlfix last 7 days additions', choices=(countries))
    if CountrySelect == "Argentina":
         CountryShortCode="ar"
         Last7daysNews()
    elif CountrySelect =="Belgium":
         CountryShortCode="be"
         Last7daysNews()
    elif CountrySelect == "Brazil":
         CountryShortCode = "br"
         Last7daysNews()
    elif CountrySelect == "Canada":
         CountryShortCode = "ca"
         Last7daysNews()
    elif CountrySelect == "Czech Republic":
         CountryShortCode = "cz"
         Last7daysNews()
    elif CountrySelect == "France":
         CountryShortCode = "fr"
         Last7daysNews()
    elif CountrySelect == "Germany":
         CountryShortCode = "de"
         Last7daysNews()
    elif CountrySelect == "Greece":
         CountryShortCode = "gr"
         Last7daysNews()
    elif CountrySelect == "Hong Kong":
         CountryShortCode = "hk"
         Last7daysNews()
    elif CountrySelect == "Iceland":
         CountryShortCode = "is"
         Last7daysNews()
    elif CountrySelect == "India":
         CountryShortCode = "in"
         Last7daysNews()
    elif CountrySelect == "Israel":
         CountryShortCode = "il"
         Last7daysNews()
    elif CountrySelect == "Italy":
         CountryShortCode = "it"
         Last7daysNews()
    elif CountrySelect == "Japan":
         CountryShortCode = "jp"
         Last7daysNews()
    elif CountrySelect == "Lithuania":
         CountryShortCode = "lt"
         Last7daysNews()
    elif CountrySelect == "Mexico":
         CountryShortCode = "mx"
         Last7daysNews()
    elif CountrySelect == "Netherlands":
         CountryShortCode = "nl"
         Last7daysNews()
    elif CountrySelect == "Poland":
         CountryShortCode = "pl"
         Last7daysNews()
    elif CountrySelect == "Portugal":
         CountryShortCode = "pt"
         Last7daysNews()
    elif CountrySelect == "Romania":
         CountryShortCode = "ro"
         Last7daysNews()
    elif CountrySelect == "Russia":
         CountryShortCode = "ru"
         Last7daysNews()
    elif CountrySelect == "Singapore":
         CountryShortCode = "sg"
         Last7daysNews()
    elif CountrySelect == "Slovakia":
         CountryShortCode = "sk"
         Last7daysNews()
    elif CountrySelect == "South Africa":
         CountryShortCode = "za"
         Last7daysNews()
    elif CountrySelect == "South Korea":
         CountryShortCode = "kr"
         Last7daysNews()
    elif CountrySelect == "Spain":
         CountryShortCode = "es"
         Last7daysNews()
    elif CountrySelect == "Sweden":
         CountryShortCode = "se"
         Last7daysNews()
    elif CountrySelect == "Switzerland":
         CountryShortCode = "ch"
         Last7daysNews()
    elif CountrySelect == "Thailand":
         CountryShortCode = "th"
         Last7daysNews()
    elif CountrySelect == "United Kingdom":
         CountryShortCode = "gb"
         Last7daysNews()
    elif CountrySelect == "United States":
         CountryShortCode = "us"
         Last7daysNews()
    else:
        sys.exit(0)

def Last7daysNews():
    try:
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
            New7Movies = New7Movies + (ListNewJson["ITEMS"][count]["title"])+str(" - Added the :") \
                         +str(ListNewJson["ITEMS"][count]["unogsdate"])+str(" Type : ") \
                         +str(ListNewJson["ITEMS"][count]["type"])+str("\n")
            count = count + 1
            if count > key-1:
                break
        New7Movies = New7Movies +str("\n\nDeveloper : Hamdy Abou El Anein\nhttps://www.github.com/hamdyaea\nhttp://www.daylightlinux.ch")
        image = netflixLogo
        title = "The last 7 days adds on Netflix for "+str(CountrySelect)
        msg = New7Movies
        choices = ["OK"]
        reply = buttonbox(image=image, msg=msg, choices=choices, title=title)
    except:
        print("Error : impossible to connect to the Netflix API")

ListCountry()
