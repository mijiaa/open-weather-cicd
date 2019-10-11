import sys
# import requests
import urllib.request
import json
API ="170dae04cac7827d30fd3679c496ffb4"
command_arg = sys.argv

#process data commands
data_command_lst = ["-time", "-temp", "pressure", "-cloud", "-humidity", "-wind", "sunset", "-sunrise", "-help"]
loc_command_lst = ['-city', '-z', '-gc', 'cid']

def check_command_args(command_arg):
    # initialize global variables for each command
    api, help, help_error= False, False,False # first argument check
    city, c_id, zip, geo = False, False, False, False # location check
    time, temp, temp_cel,pressure, cloud, humidity, wind, sunset, sunrise = False, False, False, False, False, False, False, False, False # data check
    city_res, id_res, zip_res, geo_res = None, None, None, None # data results
    duplicate_data,  duplicate_loc  = False, False # duplicates

    # check if first argument is right
    first_arg= command_arg[1].split('=')[0]
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
                if city:
                    city = False
                    duplicate_loc = True
                else:
                    city = True
                    city_res = data
            elif command == '-cid':
                if c_id:
                    c_id = False
                    duplicate_loc = True
                else:
                    c_id = True
                    id_res= data
            elif command == '-z':
                if zip:
                    zip = False
                    duplicate_loc = True
                else:
                    zip = True
                    zip_res= data
            elif command == '-gc':
                if geo:
                    geo = False
                    duplicate_loc = True
                else:
                    geo = True
                    geo_res = data

            elif command == '-time':
                if geo:
                    time = False
                    duplicate_data = True
                else:
                    time = True

            elif command == 'temp':
                temp = True
                temp_cel = True
                if data == 'farenheit':
                    temp_cel = False
                elif data == 'celcius':
                    temp_cel == True

            elif command == '-pressure':
                if pressure:
                    pressure = False
                    duplicate_data = True
                else:
                    pressure = True

            elif command == '-cloud':
                if cloud:
                    cloud = False
                    duplicate_data = True
                else:
                    cloud = True
            elif command == '-humidity':
                if humidity:
                    humidity = False
                    duplicate_data=True
                else:
                    humid = True
            elif command == '-wind':
                if wind:
                    wind = False
                    duplicate_data = True
                else:
                    wind = True
            elif command == '-sunset':
                if sunset:
                    sunset = False
                    duplicate_data=True
                else:
                    sunset = True
            elif command == '-sunrise':
                if sunrise:
                    sunrise = False
                    duplicate_data = True
                else:
                    sunrise = True
            elif command == '-help':
                duplicate_data = True
                help_error = True

    first_arg_lst = [ api, help, help_error]
    location_check_lst=[ city, c_id, zip, geo ]
    data_check_lst=[ time, temp, temp_cel,pressure, cloud, humidity, wind, sunset, sunrise]
    data_result_lst =[ city_res, id_res, zip_res, geo_res]
    duplicate_check_lst = [duplicate_data,  duplicate_loc]

    return first_arg_lst, location_check_lst, data_check_lst,data_result_lst, duplicate_check_lst




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

