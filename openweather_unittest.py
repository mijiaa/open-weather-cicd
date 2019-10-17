from openweather import *
import unittest
from unittest import mock


# Test class to test the check_command_args
class CheckCommandArgsTestCases(unittest.TestCase):
    # Check if the user didn't enter in any comments
    def test_no_commands(self):
        commands = ['openweather.py']
        self.assertRaisesRegex(Exception,  "Enter in some commands to get data from a location or use the -help command.", check_command_args, commands)

    # Check if user enter an input for commands that do not allow input
    def test_no_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunset=time']
        self.assertRaisesRegex(Exception, "Only the commands -api, -city, -cid, -gc, -z and -temp allows inputs.", check_command_args, commands)

    # Check if user enter an input for commands that allow input
    def test_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city']
        self.assertRaisesRegex(Exception, "Please enter an input using a '=' after the command.\nEg. -city=London", check_command_args, commands)

    # Check if user entered any invalid commands
    def test_invalid_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-what']
        self.assertRaisesRegex(Exception, "Commands aren't spelled correctly.", check_command_args, commands)

    # Check if there was mutiple -api commands
    def test_multiple_api_command(self):
        commands = ['openweather.py', '-city=London', '-api=170dae04cac7827d30fd3679c496ffb4', '-api=170dae04cac7827d30fd3679c496ffb4']
        self.assertRaisesRegex(Exception, "Multiple chosen API keys given are specified.", check_command_args, commands)

    # Check if command -city is working
    def test_city_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London','-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -city is wrong.")

    # Check if command -cid is working
    def test_cid_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-cid=2172797', '-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [False, True, False, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '2172797']]
        self.assertEqual(result, actual_result, "The checking of the -cid is wrong.")

    # Check if command -gc is working
    def test_gc_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-gc=35,139','-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [False, False, False, True], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '35,139']]
        self.assertEqual(result, actual_result, "The checking of the -gc is wrong.")

    # Check if command -z is working
    def test_zip_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-z=94040,us','-sunrise']
        result = check_command_args(commands)
        actual_result =[False, [False, False, True, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '94040,us']]
        self.assertEqual(result, actual_result, "The checking of the -z is wrong.")

    # Check if the exception is raised in the city check
    def test_multi_city_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunrise', '-city=London']
        self.assertRaisesRegex(Exception,  "Multiple chosen locations are specified.", check_command_args, commands)

    # Check if the exception is raised in the cid check
    def test_multi_cid_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-sunrise', '-city=London', '-cid=2172797']
        self.assertRaisesRegex(Exception,  "Multiple chosen locations are specified.", check_command_args, commands)

    # Check if the exception is raised in the gc check
    def test_multi_gc_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-z=94040,us','-sunrise', '-gc=35,129']
        self.assertRaisesRegex(Exception,  "Multiple chosen locations are specified.", check_command_args, commands)

    # Check if the exception is raised in the z check
    def test_multi_zip_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4','-sunrise', '-city=London', '-z=94040,us']
        self.assertRaisesRegex(Exception,  "Multiple chosen locations are specified.", check_command_args, commands)

    # Check if the -help command is functioning
    def test_help_command(self):
        commands = ['openweather.py', '-help']
        result = check_command_args(commands)
        actual_result = [True, [False, False, False, False], [False, False, True, False, False, False, False, False, False], [None, None]]
        self.assertEqual(result, actual_result, "The checking of the -help is wrong.")

    # Check if the checking of multiple -humidity is functioning
    def test_invalid_help_command(self):
        commands = ['openweather.py', '-help', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time']
        self.assertRaisesRegex(Exception, "-help command can only be called alone. ", check_command_args, commands)

    # Check if the -time command is functioning
    def test_time_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -time is wrong.")

    # Check if the checking of multiple -time is functioning
    def test_multiple_time_command(self):
        commands = ['openweather.py', '-time', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time']
        self.assertRaisesRegex(Exception, "Multiple -time commands are specified.", check_command_args, commands)

    # Check if the default of the -temp command is functioning
    def test_temp_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-temp']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, True, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -temp is wrong.")

    # Check if the default of the -temp command is functioning
    def test_temp_celsius_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-temp=celsius']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, True, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -temp command with the input of celsius is wrong.")

    # Check if the default of the -temp command is functioning
    def test_temp_fahrenheit_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-temp=fahrenheit']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, True, False, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -temp command with the input of fahrenheit is wrong.")

    # Check if the default of the -temp command is functioning
    def test_temp_random_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-temp=testing']
        self.assertRaisesRegex(Exception, "Wrong unit of temperature. Either in fahrenheit or celsius.", check_command_args, commands)

    # Check if the checking of multiple -temp is functioning
    def test_multiple_temp_command(self):
        commands = ['openweather.py', '-temp=fahrenheit', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-temp']
        self.assertRaisesRegex(Exception, "Multiple -temp commands are specified.", check_command_args, commands)

    # Check if the default of the -pressure command is functioning
    def test_pressure_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-pressure']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, True, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -pressure is wrong.")

    # Check if the checking of multiple -pressure is functioning
    def test_multiple_pressure_command(self):
        commands = ['openweather.py', '-pressure', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-pressure']
        self.assertRaisesRegex(Exception, "Multiple -pressure commands are specified.", check_command_args, commands)

    # Check if the default of the -cloud command is functioning
    def test_cloud_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-cloud']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, False, True, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -cloud is wrong.")

    # Check if the checking of multiple -cloud is functioning
    def test_multiple_cloud_command(self):
        commands = ['openweather.py', '-cloud', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-cloud']
        self.assertRaisesRegex(Exception, "Multiple -cloud commands are specified.", check_command_args, commands)

    # Check if the default of the -humidity command is functioning
    def test_humidity_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-humidity']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, False, False, True, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -humidity is wrong.")

    # Check if the checking of multiple -humidity is functioning
    def test_multiple_humidity_command(self):
        commands = ['openweather.py', '-humidity', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-humidity']
        self.assertRaisesRegex(Exception, "Multiple -humidity commands are specified.", check_command_args, commands)

    # Check if the default of the -wind command is functioning
    def test_wind_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-wind']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, False, False, False, True, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -wind is wrong.")

    # Check if the checking of multiple -wind is functioning
    def test_multiple_wind_command(self):
        commands = ['openweather.py', '-wind', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-wind']
        self.assertRaisesRegex(Exception, "Multiple -wind commands are specified.", check_command_args, commands)

    # Check if the default of the -sunset command is functioning
    def test_sunset_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunset']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, False, False, False, False, True, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -sunset is wrong.")

    # Check if the checking of multiple -sunset is functioning
    def test_multiple_sunset_command(self):
        commands = ['openweather.py', '-sunset', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunset']
        self.assertRaisesRegex(Exception, "Multiple -sunset commands are specified.", check_command_args, commands)

    # Check if the default of the -sunrise command is functioning
    def test_sunrise_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -sunrise is wrong.")

    # Check if the checking of multiple -humidity is functioning
    def test_multiple_sunrise_command(self):
        commands = ['openweather.py', '-sunrise', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunrise']
        self.assertRaisesRegex(Exception, "Multiple -sunrise commands are specified.", check_command_args, commands)

    # check if user enter api key
    def test_no_api_command(self):
        commands = ['openweather.py', '-city=London']
        self.assertRaisesRegex(Exception, "API key is was not inputted. You may add it with the -api command", check_command_args, commands)

    # Check whether one input is valid
    def test_check_input_check_with_one_input(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the data commands is wrong.")

    # Check whether multiple input is valid
    def test_check_input_check_with_more_than_one_input(self):
        commands = ['openweather.py', '-pressure', '-api=170dae04cac7827d30fd3679c496ffb4', '-sunset', '-city=London', '-time']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [True, False, True, True, False, False, False, True, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the data commands is wrong.")

    # Check whether no data commands is valid
    def test_check_input_check_with_no_input(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London']
        self.assertRaisesRegex(Exception, "Enter in some data commands or call the -help command.", check_command_args, commands)


# Test class to test the display_message function
class DisplayingMessageTestCases(unittest.TestCase):
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        # To be by most of the test cases
        if args[0] == 'http://api.openweathermap.org/data/2.5/weather?appid=170dae04cac7827d30fd3679c496ffb4&q=London':
            return MockResponse({'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 287.13, 'pressure': 1001, 'humidity': 87, 'temp_min': 284.82, 'temp_max': 290.37}, 'visibility': 10000, 'wind': {'speed': 6.7, 'deg': 280}, 'rain': {}, 'clouds': {'all': 75}, 'dt': 1571218509, 'sys': {'type': 1, 'id': 1502, 'country': 'GB', 'sunrise': 1571207117, 'sunset': 1571245602}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}, 200)
        # To be used when checking for the -cid command
        elif args[0] == 'http://api.openweathermap.org/data/2.5/weather?appid=170dae04cac7827d30fd3679c496ffb4&id=2172797':
            return MockResponse({'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 281.01, 'pressure': 1007, 'humidity': 87, 'temp_min': 278.15, 'temp_max': 283.15}, 'visibility': 10000, 'wind': {'speed': 1.5}, 'rain': {}, 'clouds': {'all': 59}, 'dt': 1571290727, 'sys': {'type': 1, 'id': 1414, 'country': 'GB', 'sunrise': 1571293620, 'sunset': 1571331874}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}, 200)

        return MockResponse(None, 404)

    # Test if the city's concatenation of the base url, API key and the user's input for the city command is correct
    def test_get_city_json(self):
        output_result = displaying_message(False, [True, False, False, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London'])
        self.assertEqual(output_result[1].status_code, 200, "There is a problem getting the JSON using the -city command.")

    # Test if the cid's concatenation of the base url, API key and the user's input for the cid command is correct
    def test_get_cid_json(self):
        output_result = displaying_message(False, [False, True, False, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', '2172797'])
        self.assertEqual(output_result[1].status_code, 200, "There is a problem getting the JSON using the -cid command.")

    # Test if the gc's concatenation of the base url, API key and the user's input for the gc command is correct
    def test_get_gc_json(self):
        output_result = displaying_message(False, [False, False, False, True], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', '35,139'])
        self.assertEqual(output_result[1].status_code, 200, "There is a problem getting the JSON using the -gc command.")

    # Test if the z's concatenation of the base url, API key and the user's input for the z command is correct
    def test_get_z_json(self):
        output_result = displaying_message(False, [False, False, True, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', '94040,us'])
        self.assertEqual(output_result[1].status_code, 200, "There is a problem getting the JSON using the -cid command.")

    # Test whether the user didn't enter any location commands
    def test_no_location_commands_given(self):
        arg = False, [False, False, False, False], [False, True, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', None]
        self.assertRaisesRegex(Exception, "Please enter a location command.", displaying_message, arg[0], arg[1], arg[2], arg[3])

    # Test whether user input is the wrong format for the gc command
    def test_incorrect_input_format_gc(self):
        arg = False, [False, False, False, True], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', '39&139']
        self.assertRaisesRegex(Exception, "When entering the latitude and longitude coordinates for this command, separate them with a ','", displaying_message, arg[0], arg[1], arg[2], arg[3])

    # Test whether user input is missed the country code for the z command
    def test_incorrect_input_format_z(self):
        arg = False, [False, False, True, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', '94040']
        self.assertRaisesRegex(Exception, "When entering the zip code and the country code for this command, separate them with a ','", displaying_message, arg[0], arg[1], arg[2], arg[3])

    # Test if the user has enter a non existent city name
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_user_input(self, mock_get):
        arg = False, [True, False, False, False], [False, True, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'test']
        self.assertRaisesRegex(Exception, "Entered in wrong inputs given to the commands.", displaying_message, arg[0], arg[1], arg[2], arg[3])

    # Test if Json data process for temp=fahrenheit is correct
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_temp_fahrenheit(self, mock_get):
        output_str = displaying_message(False, [True, False, False, False], [False, True, False, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London'])
        actual_output_str = "The temperature ranges from 33.88 to 33.91 fahrenheit."
        self.assertEqual(output_str[0], actual_output_str, "JSON data handling for fahrenheit has error")

    # Test if Json data process for temp=celsius is correct
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_temp_celsius(self, mock_get):
        output_str = displaying_message(False, [True, False, False, False], [False, True, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London'])
        actual_output_str = "The temperature ranges from 11.67 to 17.22 celsius."
        self.assertEqual(output_str[0], actual_output_str, "JSON data handling for fahrenheit has error")

    # Test if Json data process for wind speed is correct
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_wind_speed(self, mock_get):
        output_str = displaying_message(False, [False, True, False, False], [False, False, True, False, False, False, True, False, False], ['170dae04cac7827d30fd3679c496ffb4', '2172797'])
        actual_output_str = "A wind speed of 1.5m/s."
        self.assertEqual(output_str[0], actual_output_str, "JSON data handling for wind speed has error")

    # Test if Json data process for wind speed and angle is correct
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_wind_angle(self, mock_get):
        output_str = displaying_message(False, [True, False, False, False], [False, False, False, False, False, False, True, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London'])
        actual_output_str = "A wind speed of 6.7m/s from 280 degrees."
        self.assertEqual(output_str[0], actual_output_str, "JSON data handling for fahrenheit has error")

    # Test if overall Json data process output is correct except for temp
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        output_str = displaying_message(False, [True, False, False, False], [True, False, True, True, True, True,False, True, True], ['170dae04cac7827d30fd3679c496ffb4', 'London'])
        actual_output_str = "Time of weather shown is on 2019-10-16 9:35:9." \
                            "The atmospheric pressure is 1001hPa.It is likely to be broken clouds with a cloudiness of 75%." \
                            "It is likely to be broken clouds with a humidity of 75%." \
                            "The sun sets at 17:6:42.The sun rises at 6:25:17."
        self.assertEqual(output_str[0], actual_output_str, "JSON data handling has error")


if __name__ == "__main__":
    unittest.main()
