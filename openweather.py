import sys
import time
import requests

# To get the arguments the user entered in
command_arg = sys.argv

# python openweather.py -api=170dae04cac7827d30fd3679c496ffb4


def check_command_args(command_arg):
    # Listing out all the possible command-line commands
    command_list = ["-api", "-help", "-city", "-cid", "-gc", "-z", "-time", "-temp", "-pressure", "-cloud", "-humidity", "-wind", "-sunset", "-sunrise"]

    # Initialize variables for each command, check for each command
    api, help = False, False
    city, cid, zip, geo = False, False, False, False
    time, temp, pressure, cloud, humidity, wind, sunset, sunrise = False, False, False, False, False, False, False, False

    # To hold the user input
    # api_data is to holds the API key user entered in
    # loc_data is to hold the locations data
    # temp_data is to check whether its is celsius or fahrenheit. temp_data is True if it is celsius anf vice versa.
    api_data, loc_data, temp_data = None, None, True

    # check_data_inputs checks for whether the user entered any data commands
    # check_loc check whether there is a repeat of location commands
    check_data_inputs, check_loc = False, False

    # Check whether user hasn't entered in any arguments other than the file name
    if len(command_arg) < 1:
        raise Exception("Enter in some commands to get data from a location or use the -help command.")

    for i in range(1, len(command_arg)):
        # Check whether the user entered in an input along with a command
        if "=" in command_arg[i]:
            command_split = command_arg[i].split('=')
            command = command_split[0]
            data = command_split[1]

            # Check whether the command is one of this commands
            if command not in ['-api', '-city', '-z', '-gc', '-cid', '-temp']:
                raise Exception("Only the commands -api, -city, -cid, -gc, -z and -temp allows inputs.")
        else:
            # Command that doesn't need a input
            command = command_arg[i]
            data = None

            if command in ['-api', '-city', '-z', '-gc', '-cid']:
                raise Exception("Please enter an input using a '=' after the command.\nEg. -city=London")

        # Check if the command exist in the list of commands
        if command not in command_list:
            raise Exception("Commands aren't spelled correctly.")

        elif command == "-api":
            # Check if -api was called before
            if api:
                raise Exception("Multiple chosen API keys given are specified.")
            else:
                api = True
                api_data = data
        elif command == '-city':
            # Check whether a location command was called before
            if check_loc:
                raise Exception("Multiple chosen locations are specified.")
            else:
                city = True
                loc_data = data
                check_loc = True
        elif command == '-cid':
            if check_loc:
                raise Exception("Multiple chosen locations are specified.")
            else:
                cid = True
                loc_data = data
                check_loc = True
        elif command == '-z':
            if check_loc:
                raise Exception("\nMultiple chosen locations are specified.")
            else:
                zip = True
                loc_data = data
                check_loc = True
        elif command == '-gc':
            if check_loc:
                raise Exception("Multiple chosen locations are specified.")
            else:
                geo = True
                loc_data = data
                check_loc = True
        elif command == '-time':
            # Check whether the time command was called before
            if time:
                raise Exception("Multiple -time commands are specified.")
            else:
                time = True
                # To check whether the user mentioned any data they want to display
                check_data_inputs = True
        elif command == '-temp':
            if temp:
                raise Exception("Multiple -temp commands are specified.")
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
                # User misspelled the unit or gave the wrong unit
                else:
                    raise Exception("Wrong unit of temperature. Either in fahrenheit or celsius.")
        elif command == '-pressure':
            if pressure:
                raise Exception("Multiple -pressure commands are specified.")
            else:
                pressure = True
                check_data_inputs = True
        elif command == '-cloud':
            if cloud:
                raise Exception("Multiple -cloud commands are specified.")
            else:
                cloud = True
                check_data_inputs = True
        elif command == '-humidity':
            if humidity:
                raise Exception("Multiple -humidity commands are specified.")
            else:
                humidity = True
                check_data_inputs = True
        elif command == '-wind':
            if wind:
                raise Exception("Multiple -wind commands are specified.")
            else:
                wind = True
                check_data_inputs = True
        elif command == '-sunset':
            if sunset:
                raise Exception("Multiple -sunset commands are specified.")
            else:
                sunset = True
                check_data_inputs = True
        elif command == '-sunrise':
            if sunrise:
                raise Exception("Multiple -sunrise commands are specified.")
            else:
                sunrise = True
                check_data_inputs = True
        elif command == '-help':
            # Check if the first argument is -help
            if len(command_arg) == 2:
                help = True
                check_data_inputs = True
            else:
                # -help can't be called with other commands
                raise Exception("-help command can only be called alone. ")

    # Check whether the user entered any data to display
    if check_data_inputs:
        location_check_lst = [city, cid, zip, geo]
        data_check_lst = [time, temp, temp_data, pressure, cloud, humidity, wind, sunset, sunrise]
        user_inputs = [api_data, loc_data]

        # To display the data commands
        displaying_message(help, location_check_lst, data_check_lst, user_inputs)

        return [help, location_check_lst, data_check_lst, user_inputs]
    else:
        raise Exception("Enter in some data commands or call the -help command.")


def displaying_message(help, location_check_lst, data_check_lst, user_inputs):
    if help:
        print("\n-api=<API_key> : where you should put the API key in the <API_key> part. \n" +
              "-help can only be called alone, meaning it can't be called with other commands. \n" +
              "\nThere are 4 commands to pick the location of the data you want to look into and they are: \n" +
              "   -city=<city_name> : the city’s name of that location, \n" +
              "   -cid=<city_id> : the city’s id of that location, \n" +
              "   -gc=<geographic_coordinates> : the latitude and longitude of that location \n" +
              "   -z=<zip_code> : the zip code of that location.\n" +
              "\nAfter choosing a location command, you have 8 information commands and they are: \n" +
              "   -time : the time when the data was taken, \n" +
              "   -temp : the temperature range of the location default is in celsius, if there are no inputs stated. \n" +
              "   -pressure : the air pressure in that location, \n" +
              "   -cloud :  the number of clouds present at the location, \n" +
              "   -humidity: the humidity of the location, \n" +
              "   -wind : the wind speed and the angle of the wind, \n" +
              "   -sunset : the time the sun settled at the location, \n" +
              "   -sunrise : the time the sun rises at that location.")
        return

    [api_key, loc_data] = user_inputs

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    if location_check_lst[0]:
        city_name = loc_data
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    elif location_check_lst[1]:
        city_id = loc_data
        complete_url = base_url + "appid=" + api_key + "&id=" + city_id
    elif location_check_lst[2]:
        if "," in loc_data:
            zip_code = loc_data
            complete_url = base_url + "appid=" + api_key + "&zip=" + zip_code
        else:
            raise ValueError("\nWhen entering the zip code and the country code for this command, separate them with a ','")
    elif location_check_lst[3]:
        if "," in loc_data:
            geo = loc_data.split(',')
            lat = geo[0]
            lon = geo[1]
            complete_url = base_url + "appid=" + api_key + "&lat=" + lat + "&lon=" + lon
        else:
            raise ValueError("When entering the latitude and longitude coordinates for this command, separate them with a ','")
    else:
        # If the user never mentioned any location commands
        raise Exception("Please enter a location command")

    response = requests.get(complete_url)
    if response.status_code == 404:
        raise ValueError("Entered in wrong inputs given to the commands.")

    json_result = response.json()

    [time, temp, temp_data, pressure, cloud, humidity, wind, sunset, sunrise] = data_check_lst

    print("\n  ")

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
        print("The atmospheric pressure is " + str(pressure_result) + "hPa. ")
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
        time_string = get_time_string(json_result['sys']['sunrise'])
        print("The sun rises at " + time_string)


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

# To execute the program
if __name__ == "__main__":
    print(check_command_args(command_arg))
