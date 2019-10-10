import sys
# import requests
import urllib.request
import json
API ="170dae04cac7827d30fd3679c496ffb4"
command_arg = sys.argv



#process data commands
data_command_lst = ["-time", "-temp", "pressure", "-cloud", "-humidity", "-wind", "sunset", "-sunrise", "-help"]
loc_command_lst = ['-city', '-z', '-gc', 'cid']
result = []

#initialize global variables for each command
api, help = False,False
city, c_id, zip, geo = False,False,False,False
time ,temp, pressure, cloud, humidity, wind, sunset, sunrise = False,False,False,False,False,False,False,False
city_res, id_res, zip_res, geo_res, temp_res = None, None, None, None, None

#check if first argument is right
first_arg= command_arg[0].split('=')[0]
if first_arg is '-api':
    api = True
elif first_arg is '-help':
    help = True

if api is True:
    for i in range(2, len(command_arg)):
        command_split = command_arg[i].split('=')
        command = command_split[0]
        data = command_split[1]
        if command not in data_command_lst and command not in loc_command_lst :
            raise Exception("data command entered is not valid ")
        elif command == '-city':
            city = True
            city_res = data
        elif command == '-cid':
            c_id = True
            id_res= data
        elif command == '-z':
            zip = True
            zip_res = data
        elif command == '-gc':
            geo = True
            geo_res = data
        elif command == '-time':
            time = True
        elif command == 'temp':
            temp = True
        elif command == '-temp' and data == 'fahrenheit':
            temp_f = True
        elif command == '-temp' and data == 'celcius':
            temp_c = True
        elif command == '-pressure':
            pressure = True
        elif command == '-cloud':
            cloud = True
        elif command == '-humidity':
            humid = True
        elif command == '-wind':
            wind = True
        elif command == '-sunset':
            sunset = True
        elif command == '-sunrise':
            sunrise  = True





# command_city = command_arg[2].split("=")
# if command_city[1] == " ":
#     raise Exception("spaces are found between command data")
#
# base_url = "http://api.openweathermap.org/data/2.5/weather?"
# if command_city[0] == "-city":
#     city_name = command_city[1]
#     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#
# elif command_city[0] == "-cid":
#     city_code = command_city[1]
#     complete_url = base_url + "appid=" + api_key + "&id=" + city_code
# elif command_city[0] == "-z":
#     city_zipcode = command_city[1]
#     complete_url = base_url + "appid=" + api_key + "&zip=" +  city_zipcode
#     #api.openweathermap.org/data/2.5/weather?zip=94040,us, zip code
# # elif  comm
# #
# # se
# else :
#     raise Exception("location command entered is not valid")

#
# #making json requests
# response = urllib.request.urlopen(complete_url)
# json_res = json.loads(response.read())
# def data_command_process(lst,index):
#     if lst[index] == "-time":
#         output_result.append(json_res["time"])
#     if lst

