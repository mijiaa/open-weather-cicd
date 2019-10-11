import sys
# import requests
import urllib.request
import json
import time
from urllib.error import HTTPError

API = "170dae04cac7827d30fd3679c496ffb4"
command_arg = sys.argv

# process data commands
data_command_lst = ["-time", "-temp", "pressure", "-cloud", "-humidity", "-wind", "sunset", "-sunrise", "-help"]
loc_command_lst = ['-city', '-z', '-gc', 'cid']


def check_command_args(command_arg):
    # initialize global variables for each command
    api, api_data, help, help_check = False, None, False, False # first argument check
    city, c_id, zip, geo = False, False, False, False # location check
    time, temp, temp_data, pressure, cloud, humidity, wind, sunset, sunrise = False, False, True, False, False, False, False, False, False # data check
    city_res, id_res, zip_res, geo_res = None, None, None, None # data results
    check_valid, check_inputs = True, False

    if len(command_arg) <= 1:
        print("Enter in some commands to get data from a location or get help. ")
        return

    # check if first argument is right
    if "=" in command_arg[1]:
        command_split = command_arg[1].split('=')
        command = command_split[0]
        data = command_split[1]

        if command == '-api':
            api = True
            api_data = data
    elif command_arg[1] == "-help":
        help = True
    else:
        print("The -api command along with the API key must be the first argument or the -help command")
        return

    if api:
        for i in range(2, len(command_arg)):
            if "=" in command_arg[i]:
                command_split = command_arg[i].split('=')
                command = command_split[0]
                data = command_split[1]
            else:
                command = command_arg[i]

            check_inputs = True
            if command not in data_command_lst and command not in loc_command_lst:
                print("Commands aren't spelled correctly or entered in the correct format")
                check_valid = False
                return
            elif command == "-api":
                if api:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
            elif command == '-city':
                if city:
                    print("Multiple chosen locations are specified.")
                    check_valid = False
                    return
                else:
                    city = True
                    city_res = data
            elif command == '-cid':
                if c_id:
                    print("Multiple chosen locations are specified.")
                    check_valid = False
                    return
                else:
                    c_id = True
                    id_res = data
            elif command == '-z':
                if zip:
                    print("Multiple chosen locations are specified.")
                    check_valid = False
                    return
                else:
                    zip = True
                    zip_res = data
            elif command == '-gc':
                if geo:
                    print("Multiple chosen locations are specified.")
                    check_valid = False
                    return
                else:
                    geo = True
                    geo_res = data
            elif command == '-time':
                if geo:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    time = True
            elif command == 'temp':
                if temp:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    temp = True
                    if data == 'fahrenheit':
                        temp_data = False
                    elif data == 'celsius':
                        temp_data = True
                    else:
                        print("Wrong unit of temperature. Either fahrenheit or celsius.")
            elif command == '-pressure':
                if pressure:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    pressure = True
            elif command == '-cloud':
                if cloud:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    cloud = True
            elif command == '-humidity':
                if humidity:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    humidity = True
            elif command == '-wind':
                if wind:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    wind = True
            elif command == '-sunset':
                if sunset:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    sunset = True
            elif command == '-sunrise':
                if sunrise:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    sunrise = True
            elif command == '-help':
                if help:
                    print("Multiple chosen data are specified.")
                    check_valid = False
                    return
                else:
                    help = True

        if check_valid and check_inputs:
            first_arg_lst = [api_data, help]
            location_check_lst = [city, c_id, zip, geo]
            data_check_lst = [time, temp, temp_data, pressure, cloud, humidity, wind, sunset, sunrise]
            loc_result_lst = [city_res, id_res, zip_res, geo_res]

            displaying_message(first_arg_lst, location_check_lst, data_check_lst, loc_result_lst)
    else:
        print("The -api command must be the first argument. ")
        return

    if not check_inputs:
        print("Enter in some command to get data from a location or get help. ")
        return

    if not check_valid:
        print("There cant be multiple commands that are the same")




def displaying_message(first_arg_lst, location_check_lst, data_check_lst, loc_result_lst):
    try:
        api_key = first_arg_lst[0]
        if location_check_lst[0]:
            city_name = loc_result_lst[0]
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        elif location_check_lst[1]:
            city_id = loc_result_lst[1]
            complete_url = base_url + "appid=" + api_key + "&id=" + city_id
        elif location_check_lst[2]:
            zip_code = loc_result_lst[2]
            complete_url = base_url + "appid=" + api_key + "?zip=" + zip_code
        else:
            geo = loc_result_lst[3].split(',')
            lat = geo[0]
            lon = geo[1]
            complete_url = base_url + "appid=" + api_key + "&lat=" + lat + "&lon" + lon

        response = urllib.request.urlopen(complete_url)
        json_result = json.loads(response.read())
        print(json_result)

        if first_arg_lst[1]:
            print("-api must be always be the first command to enter in. -help can only be called with the commands -api "
                  "and a single location command. \n" + "To use this program there are 4 ways pick the location of the " +
                  "data you want to look into and they are: -city( city name) : the city’s name of that location, -cid " +
                  "(city’s id ) : the city’s id of that location, -gc ( geographic coordinates ) : the latitude and " +
                  "longitude of that location and -z ( zip code ) : the zip code of that location.\n" + "After choosing " +
                  "a location using one of the 4 location options, you have 8 data options and they are : -time : the " +
                  "time when the data was taken, -temp( in Celsius) : the temperature range of the location, -pressure : " +
                  "the air pressure in that location, -cloud :  the number of clouds present at the location, -humidity: the " +
                  "humidity of the location, -wind : the wind speed and the angle of the wind, -sunset : the time the sun " +
                  "settled at the location and -sunrise : the time the sun rises at that location.")
        else:
            [time, temp, temp_data, pressure, cloud, humidity, wind, sunset, sunrise] = data_check_lst
            if time:
                time_string = get_date_and_time_string(json_result.dt)
                print(time_string)
            elif temp:
                temp_min = json_result.main.temp_min
                temp_max = json_result.main.temp_max

                if temp_data:
                    celsius_min = temp_min - 273.15
                    celsius_max = temp_max - 273.15
                    print("The temperature ranges from " + celsius_min + " to " + celsius_max + " celsius. ")
                else:
                    fahrenheit_min = (temp_min / 273.15) * 9 / 5 + 32
                    fahrenheit_max = (temp_max / 273.15) * 9 / 5 + 32
                    print("The temperature ranges from " + fahrenheit_min + " to " + fahrenheit_max + " fahrenheit. ")
            elif pressure:
                pressure_result = json_result.main.pressure
                print("The pressure is " + pressure_result + " hPa. ")
            elif cloud:
                description =  json_result.weather.description
                cloudiness = json_result.clouds.all
                print("It likely to be " + description + "with a cloudiness of " + cloudiness + "%. ")
            elif humidity:
                description =  json_result.weather.description
                humidity_percent = json_result.clouds.all
                print("It likely to be " + description + "with a humidity of " + humidity_percent + "%. ")
            elif wind:
                wind_speed = json_result.wind.speed
                wind_angle = json_result.wind.deg
                print("A wind speed of " + wind_speed + "m/s from " + wind_angle + " degrees. ")
            elif sunset:
                time_string = get_time_string(json_result.sys.sunset)
                print("The sun sets at " + time_string)
            elif sunrise:
                time_string = get_time_string(json_result.sys.sunset)
                print("The sun sets at " + time_string)
    except HTTPError:
        print("Wrong inputs given to the commands.")


def get_date_and_time_string(seconds):
    result = time.localtime(seconds)

    time_string = "On "

    time_string += result.tm_year + "-"
    time_string += result.tm_mon + "-"
    time_string += result.tm_mday + " "

    time_string += result.tm_hour + ":"
    time_string += result.tm_min + ":"
    time_string += result.tm_sec + ". "

    return time_string

def get_time_string(seconds):
    result = time.localtime(seconds)

    time_string = ""

    time_string += result.tm_hour + ":"
    time_string += result.tm_min + ":"
    time_string += result.tm_sec + ". "

    return time_string

# command_city = command_arg[2].split("=")
# if command_city[1] == " ":
#     raise Exception("spaces are found between command data")
#
base_url = "http://api.openweathermap.org/data/2.5/weather?"
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

check_command_args(command_arg)

# complete_url = base_url + "appid=" + API + "&lat=3.0567"  + "&lon=101.5851"
# #
# # #making json requests
# try:
#     response = urllib.request.urlopen(complete_url)
#     json_res = json.loads(response.read())
#     print(json_res)
#     print(json_res.dt)
# except HTTPError:
#     raise Exception("mreo")



