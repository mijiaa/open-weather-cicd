import sys
# import requests
import urllib.request
import json

command_arg = sys.argv

if command_arg[1] =="-help":
    help()
else:
    api_str = command_arg[1].split('=')
    api_key =  api_str[1]


command_city = command_arg[2].split("=")

base_url = "http://api.openweathermap.org/data/2.5/weather?"
if command_city[0] == "-city":
    city_name = command_city[1]
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

elif command_city[0] == "-cid":
    city_code = command_city[1]
    complete_url = base_url + "appid=" + api_key + "&id=" + city_code
elif command_city[0] == "-z":
    city_zipcode = command_city[1]
    complete_url = base_url + "appid=" + api_key + "&zip=" +  city_zipcode
    #api.openweathermap.org/data/2.5/weather?zip=94040,us, zip code
# elif  comm
#
# se
else :
    raise Exception("location command entered is not valid")

def help():
    print(" possible ")
#making json requests
response = urllib.request.urlopen(complete_url)
json_res = json.loads(response.read())

#process data commands

