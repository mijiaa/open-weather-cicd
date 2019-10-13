import sys
import urllib.request
import json
import time
from urllib.error import HTTPError

# To get the arguments the user entered in
command_arg = sys.argv

# python openweather.py -api=170dae04cac7827d30fd3679c496ffb4


def check_command_args(command_arg):
    # Listing out all the possible command-line commands
    command_list = ["-api", "-help", "-city", "-cid", "-gc", "-z", "-time", "-temp", "-pressure", "-cloud", "-humidity", "-wind", "-sunset", "-sunrise"]

    # Initialize variables for each command
    # api_data is to hold the API key user enter.
    # help_check is to check whether -help was called with the other commands that display information
    api, api_data, help, help_check = False, None, False, False
    city, c_id, zip, geo = False, False, False, False
    # temp_data is to check whether its is celsius or fahrenheit. temp_data is True if it is celsius anf vice versa.
    time, temp, temp_data, pressure, cloud, humidity, wind, sunset, sunrise = False, False, True, False, False, False, False, False, False
    # To hold the data when user inputs in for the location commands
    city_res, id_res, zip_res, geo_res = None, None, None, None
    # check_data_inputs checks for whether the user entered any data commands
    # check_loc check whether there is a repeat of location commands
    check_data_inputs, check_loc = False, False

    # Check whether user hasn't entered in any arguments other than the file name
    if len(command_arg) < 1:
        print("Enter in some commands to get data from a location or use the -help command.")
        return

    for i in range(1, len(command_arg)):
        # Check whether the user entered in an input along with a command
        if "=" in command_arg[i]:
            command_split = command_arg[i].split('=')
            command = command_split[0]
            data = command_split[1]

            # Check whether the command is one of this commands
            if command not in ['-api', '-city', '-z', '-gc', '-cid', '-temp']:
                print("\nOnly the commands -api, -city, -cid, -gc, -z and -temp allows inputs.")
                return
        else:
            # Command that doesn't need a input
            command = command_arg[i]
            data = None

        # Check if the command exist in the list of commands
        if command not in command_list:
            print("\nCommands aren't spelled correctly.")
            return
        elif command == "-api":
            # Check if -api was called before
            if api:
                print("\nMultiple chosen API keys given are specified.")
                return
            else:
                api = True
                api_data = data
        elif command == '-city':
            # Check whether a location command was called before
            if check_loc:
                print("\nMultiple chosen locations are specified.")
                return
            else:
                city = True
                city_res = data
                check_loc = True
        elif command == '-cid':
            if check_loc:
                print("\nMultiple chosen locations are specified.")
                return
            else:
                c_id = True
                id_res = data
                check_loc = True
        elif command == '-z':
            if check_loc:
                print("\nMultiple chosen locations are specified.")
                return
            else:
                zip = True
                zip_res = data
                check_loc = True
        elif command == '-gc':
            if check_loc:
                print("\nMultiple chosen locations are specified.")
                return
            else:
                geo = True
                geo_res = data
                check_loc = True
        elif command == '-time':
            # Check whether the time command was called before
            if time:
                print("\nMultiple chosen data are specified.")
                return
            else:
                time = True
                # To check whether the user mentioned any data they want to display
                check_data_inputs = True
        elif command == '-temp':
            if temp:
                print("\nMultiple chosen data are specified.")
                return
            else:
                temp = True
                check_data_inputs = True
                # Check if user wanted fahrenheit
                if data == 'fahrenheit':
                    temp_data = False
                # Check if user wanted celsius
                elif data == 'celsius':
                    temp_data = True
                elif data is None:
                    temp_data = True
                # User mispelled the unit or gave the wrong unit
                else:
                    print("\nWrong unit of temperature. Either in fahrenheit or celsius.")
                    return
        elif command == '-pressure':
            if pressure:
                print("\nMultiple chosen data are specified.")
                return
            else:
                pressure = True
                check_data_inputs = True
        elif command == '-cloud':
            if cloud:
                print("\nMultiple chosen data are specified.")
                return
            else:
                cloud = True
        elif command == '-humidity':
            if humidity:
                print("\nMultiple chosen data are specified.")
                return
            else:
                humidity = True
                check_data_inputs = True
        elif command == '-wind':
            if wind:
                print("\nMultiple chosen data are specified.")
                return
            else:
                wind = True
                check_data_inputs = True
        elif command == '-sunset':
            if sunset:
                print("\nMultiple chosen data are specified.")
                return
            else:
                sunset = True
                check_data_inputs = True
        elif command == '-sunrise':
            if sunrise:
                print("\nMultiple chosen data are specified.")
                return
            else:
                sunrise = True
                check_data_inputs = True
        elif command == '-help':
            # Check if the first argument is -help
            if len(command_arg) == 2:
                help = True
            else:
                # -help can't be called with other commands
                print("\n-help command can only be called alone. ")
                return

    # Check whether the user entered any data to display
    if check_data_inputs:
        first_arg_lst = [api_data, help]
        location_check_lst = [city, c_id, zip, geo]
        data_check_lst = [time, temp, temp_data, pressure, cloud, humidity, wind, sunset, sunrise]
        loc_result_lst = [city_res, id_res, zip_res, geo_res]

        # To display the data commands
        displaying_message(first_arg_lst, location_check_lst, data_check_lst, loc_result_lst)
    else:
        print("Enter in a location command and some data commands or call the -help command.")
        return


def displaying_message(first_arg_lst, location_check_lst, data_check_lst, loc_result_lst):
    try:
        if first_arg_lst[1]:
            print("\n-api must be always be the first command to enter in along with the API key.\n" +
                  "-help can only be called with a single -api command and a single location command. \n" +
                  "\nThere are 4 commands to pick the location of the data you want to look into and they are: \n" +
                  "   -city( city name) : the city’s name of that location, \n" +
                  "   -cid (city’s id ) : the city’s id of that location, \n" +
                  "   -gc ( geographic coordinates ) : the latitude and longitude of that location \n" +
                  "   -z ( zip code ) : the zip code of that location.\n" +
                  "\nAfter choosing a location command, you have 8 information commands and they are: \n" +
                  "   -time : the time when the data was taken, \n" +
                  "   -temp : the temperature range of the location default is in celsius, \n" +
                  "   -pressure : the air pressure in that location, \n" +
                  "   -cloud :  the number of clouds present at the location, \n" +
                  "   -humidity: the humidity of the location, \n" +
                  "   -wind : the wind speed and the angle of the wind, \n" +
                  "   -sunset : the time the sun settled at the location, \n" +
                  "   -sunrise : the time the sun rises at that location.")
            return

        api_key = first_arg_lst[0]
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        if location_check_lst[0]:
            city_name = loc_result_lst[0]
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        elif location_check_lst[1]:
            city_id = loc_result_lst[1]
            complete_url = base_url + "appid=" + api_key + "&id=" + city_id
        elif location_check_lst[2]:
            if "," in loc_result_lst[2]:
                zip_code = loc_result_lst[2]
                complete_url = base_url + "appid=" + api_key + "&zip=" + zip_code
            else:
                print("\nWhen entering the zip code and the country code for this command, separate them with a ','")
                return
        elif location_check_lst[3]:
            if "," in loc_result_lst[3]:
                geo = loc_result_lst[3].split(',')
                lat = geo[0]
                lon = geo[1]
                complete_url = base_url + "appid=" + api_key + "&lat=" + lat + "&lon=" + lon
            else:
                print("\nWhen entering the latitude and longitude coordinates for this command, separate them with a ','")
                return
        else:
            # If the user never mentioned any location commands
            print("\nPlease enter a location command")
            return

        response = urllib.request.urlopen(complete_url)
        json_result = json.loads(response.read())

        [time, temp, temp_data, pressure, cloud, humidity, wind, sunset, sunrise] = data_check_lst

        print("\n")

        if time:
            time_string = get_date_and_time_string(json_result['dt'])
            print("Time of weather shown is " + time_string)
        if temp:
            temp_min = json_result['main']['temp_min']
            temp_max = json_result['main']['temp_max']
            if temp_data:
                celsius_min = str(round(temp_min - 273.15, 2))
                celsius_max = str(round(temp_max - 273.15, 2))
                print("The temperature ranges from " + celsius_min + " to " + celsius_max + " celsius. ")
            else:
                fahrenheit_min = str(round((temp_min / 273.15) * 9 / 5 + 32, 2))
                fahrenheit_max = str(round((temp_max / 273.15) * 9 / 5 + 32, 2))
                print("The temperature ranges from " + str(fahrenheit_min) + " to " + str(fahrenheit_max) + " fahrenheit. ")
        if pressure:
            pressure_result = json_result['main']['pressure']
            print("The pressure is " + str(pressure_result) + " hPa. ")
        if cloud:
            description = json_result['weather'][0]['description']
            cloudiness = json_result['clouds']['all']
            print("It is likely to be " + str(description) + " with a cloudiness of " + str(cloudiness) + "%. ")
        if humidity:
            description =  json_result['weather'][0]['description']
            humidity_percent = json_result['clouds']['all']
            print("It is likely to be " + str(description) + " with a humidity of " + str(humidity_percent) + "%. ")
        if wind:
            wind_speed = json_result['wind']['speed']
            wind_angle = json_result['wind']['deg']
            print("A wind speed of " + str(wind_speed) + "m/s from " + str(wind_angle) + " degrees. ")
        if sunset:
            time_string = get_time_string(json_result['sys']['sunset'])
            print("The sun sets at " + time_string)
        if sunrise:
            time_string = get_time_string(json_result['sys']['sunset'])
            print("The sun sets at " + time_string)
    except HTTPError:
        print("\nWrong inputs given to the commands.")


def get_date_and_time_string(seconds):
    result = time.localtime(seconds)
    time_string = "on "

    # Getting the date
    time_string += str(result.tm_year) + "-"
    time_string += str(result.tm_mon) + "-"
    time_string += str(result.tm_mday) + " "
    # Getting the time
    time_string += str(result.tm_hour) + ":"
    time_string += str(result.tm_min) + ":"
    time_string += str(result.tm_sec) + ". "

    return time_string


def get_time_string(seconds):
    result = time.localtime(seconds)

    time_string = ""

    time_string += str(result.tm_hour) + ":"
    time_string += str(result.tm_min) + ":"
    time_string += str(result.tm_sec) + ". "

    return time_string

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



