from openweather import *
import unittest
from unittest.mock import MagicMock
from unittest import mock


class check_command_args_test(unittest.TestCase):
    def test_no_commands(self):
        commands = []
        self.assertRaisesRegex(Exception,  "Enter in some commands to get data from a location or use the -help "
                                           "command.", check_command_args, commands)

    # check if user enter an input for commands that do not allow input
    def test_no_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunset=time' ]
        self.assertRaisesRegex(Exception,
                               "Only the commands -api, -city, -cid, -gc, -z and -temp allows inputs.",
                               check_command_args, commands)

    # check if user enter api key
    def test_api_command(self):
        commands =  ['openweather.py', '-city=London']
        self.assertRaisesRegex(Exception, "API key is not found", check_command_args, commands)

    # check if user specified a location
    def test_location_input(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4']
        self.assertRaisesRegex(Exception, "Location is not specified", check_command_args, commands)

    # check if user enter an input for commands that allow input
    def test_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city']
        self.assertRaisesRegex(Exception,
                               "Please enter an input using a '=' after the command.\nEg. -city=London",
                               check_command_args, commands)

    # check if user entered any invalid commands
    def test_invalid_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-what']
        self.assertRaisesRegex(Exception,
                               "Commands aren't spelled correctly.",
                               check_command_args, commands)

    # check if command -city is working
    def test_city_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London','-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -city is wrong.")

    # check if command -z is working
    def test_zip_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-z=94040,us','-sunrise']
        result = check_command_args(commands)
        actual_result =[False, [False, False, True, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '94040,us']]
        self.assertEqual(result, actual_result, "The checking of the -z is wrong.")

    # check if command -gc is working
    def test_gc_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-gc=35,139','-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [False, False, False, True], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '35,139']]
        self.assertEqual(result, actual_result, "The checking of the -gc is wrong.")

    # check if command -cid is working
    def test_cid_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-cid=2172797', '-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [False, True, False, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '2172797']]
        self.assertEqual(result, actual_result, "The checking of the -cid is wrong.")

    # check if command -cid
    def test_multi_city_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-cid=2172797', '-sunrise', '-city=London']
        self.assertRaisesRegex(Exception,  "Multiple chosen locations are specified.", check_command_args, commands)

    def test_dup_multi_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunrise', '-city=London']
        self.assertRaisesRegex(Exception,  "Multiple chosen locations are specified.", check_command_args, commands)

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

        actual_result = [False, [True, False, False, False],
                         [False, False, True, False, False, False, True, False, False],
                         ['170dae04cac7827d30fd3679c496ffb4', 'London']]
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

    # Check if the -help command is functioning
    def test_help_command(self):
        commands = ['openweather.py', '-help']
        result = check_command_args(commands)

        actual_result = [True, [False, False, False, False], [False, False, True, False, False, False, False, False, False], [None, None]]
        self.assertEqual(result, actual_result, "The checking of the -help is wrong.")

    # Check if the checking of multiple -humidity is functioning
    def test_invalid_help_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time', '-help']

        self.assertRaisesRegex(Exception, "-help command can only be called alone. ", check_command_args, commands)

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

        actual_result = [False, [True, False, False, False], [True, False, True, True, False, False, False, True, False],
         ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the data commands is wrong.")

    # Check whether no data commands is valid
    def test_check_input_check_with_no_input(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London']
        self.assertRaisesRegex(Exception, "Enter in some data commands or call the -help command.", check_command_args, commands)


class get_json_data_test(unittest.TestCase):
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if args[0] == 'http://api.openweathermap.org/data/2.5/weather?appid=170dae04cac7827d30fd3679c496ffb4&q=London':
            return MockResponse({'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 287.13, 'pressure': 1001, 'humidity': 87, 'temp_min': 284.82, 'temp_max': 290.37}, 'visibility': 10000, 'wind': {'speed': 6.7, 'deg': 280}, 'rain': {}, 'clouds': {'all': 75}, 'dt': 1571218509, 'sys': {'type': 1, 'id': 1502, 'country': 'GB', 'sunrise': 1571207117, 'sunset': 1571245602}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}, 200)
        elif args[0] == [False, [True, False, False, False], [True, False, False, True, True, True, True, True, True], ['170dae04cac7827d30fd3679c496ffb4', 'London']]:
            return MockResponse({'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 287.13, 'pressure': 1001, 'humidity': 87, 'temp_min': 284.82, 'temp_max': 290.37}, 'visibility': 10000, 'wind': {'speed': 6.7, 'deg': 280}, 'rain': {}, 'clouds': {'all': 75}, 'dt': 1571218509, 'sys': {'type': 1, 'id': 1502, 'country': 'GB', 'sunrise': 1571207117, 'sunset': 1571245602}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}, 200)
        elif args[0] == [False, [True, False, False, False], [False, True, False, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]:
            return MockResponse({'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 287.13, 'pressure': 1001, 'humidity': 87, 'temp_min': 284.82, 'temp_max': 290.37}, 'visibility': 10000, 'wind': {'speed': 6.7, 'deg': 280}, 'rain': {}, 'clouds': {'all': 75}, 'dt': 1571218509, 'sys': {'type': 1, 'id': 1502, 'country': 'GB', 'sunrise': 1571207117, 'sunset': 1571245602}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}, 200)
        elif args[0] == [False, [True, False, False, False], [False, True,True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]:
            return MockResponse({'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 287.13, 'pressure': 1001, 'humidity': 87, 'temp_min': 284.82, 'temp_max': 290.37}, 'visibility': 10000, 'wind': {'speed': 6.7, 'deg': 280}, 'rain': {}, 'clouds': {'all': 75}, 'dt': 1571218509, 'sys': {'type': 1, 'id': 1502, 'country': 'GB', 'sunrise': 1571207117, 'sunset': 1571245602}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}, 200)

        return MockResponse(None, 404)

    # test if overall Json data process output is correct except for time
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        output_str= displaying_message(False, [True, False, False, False], [True, False, True, True, True, True, True, True, True], ['170dae04cac7827d30fd3679c496ffb4', 'London'])
        print(output_str)
        actual_output_str = "Time of weather shown is on 2019-10-16 17:35:9. " \
                            "The atmospheric pressure is 1001hPa. It is likely to be broken clouds with a cloudiness of 75%. " \
                            "It is likely to be broken clouds with a humidity of 75%. " \
                            "A wind speed of 6.7m/s from 280 degrees. " \
                            "The sun sets at 1:6:42. The sun rises at 14:25:17. "

        self.assertEqual(output_str,actual_output_str,"JSON data handling has error")

    # test if Json data process for temp=fahrenheit output is correct
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_temp_fahrenheit(self, mock_get):
        output_str = displaying_message(False, [True, False, False, False], [False, True, False, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London'])
        print(output_str)
        actual_output_str = "The temperature ranges from 33.88 to 33.91 fahrenheit. "
        self.assertEqual(output_str, actual_output_str, "JSON data handling for fahrenheit has error")

    # test if Json data process for temp=celsius output is correct
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_temp_celsius(self):
        output_str = displaying_message(False, [True, False, False, False], [False, True,True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London'])
        actual_output_str = "The temperature ranges from 12.78 to 15.56 celsius. "
        self.assertEqual(output_str, actual_output_str, "JSON data handling for fahrenheit has error")


    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_user_input(self):
        arg=  False, [True, False, False, False],[False, True, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'test']
        self.assertRaisesRegex(Exception, "Entered in wrong inputs given to the commands.", displaying_message,arg[0],arg[1],arg[2],arg[3])


if __name__ == "__main__":
    unittest.main()
