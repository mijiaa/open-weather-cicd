from openweather import *
import unittest


class openWeatherTests(unittest.TestCase):
    # Check if the -time command is functioning
    def test_time_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time']
        result = check_command_args(commands)

        actual_result = [False, [True, False, False, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -time is wrong.")

    # Check if the checking of multiple -time is functioning
    def test_multiple_time_command(self):
        commands = ['openweather.py', '-time', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time']

        self.assertRaisesRegex(Exception, "Multiple chosen data are specified.", check_command_args, commands)

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
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-temp=fahrenheit']
        result = check_command_args(commands)
        # ???
        actual_result = [False, [True, False, False, False], [False, True, False, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -temp command with the input of fahrenheit is wrong.")

    # Check if the default of the -pressure command is functioning
    def test_pressure_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-pressure']
        result = check_command_args(commands)

        actual_result = [False, [True, False, False, False], [False, False, True, True, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -pressure is wrong.")

    # Check if the default of the -cloud command is functioning
    def test_cloud_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-cloud']
        result = check_command_args(commands)

        actual_result = [False, [True, False, False, False], [False, False, True, False, True, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -cloud is wrong.")

    # Check if the default of the -humidity command is functioning
    def test_humidity_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-humidity']
        result = check_command_args(commands)

        actual_result = [False, [True, False, False, False], [False, False, True, False, False, True, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -humidity is wrong.")

    # Check if the default of the -sunset command is functioning
    def test_sunset_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunset']
        result = check_command_args(commands)

        actual_result = [False, [True, False, False, False], [False, False, True, False, False, False, False, True, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -sunset is wrong.")

    # Check if the default of the -sunrise command is functioning
    def test_sunrise_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunrise']
        result = check_command_args(commands)

        actual_result = [False, [True, False, False, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -sunrise is wrong.")

    def test_help_command(self):
        commands = ['openweather.py', '-help']
        result = check_command_args(commands)

        actual_result = [True, [False, False, False, False], [False, False, True, False, False, False, False, False, False], [None, None]]
        self.assertEqual(result, actual_result, "The checking of the -help is wrong.")

    def test_city_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London','-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [True, False, False, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -city is wrong.")

    def test_zip_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-z=94040,us','-sunrise']
        result = check_command_args(commands)
        actual_result =[False, [False, False, True, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '94040,us']]
        self.assertEqual(result, actual_result, "The checking of the -z is wrong.")

    def test_gc_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-gc=35,139','-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [False, False, False, True], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '35,139']]
        self.assertEqual(result, actual_result, "The checking of the -gc is wrong.")

    def test_cid_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-cid=2172797', '-sunrise']
        result = check_command_args(commands)
        actual_result = [False, [False, True, False, False], [False, False, True, False, False, False, False, False, True], ['170dae04cac7827d30fd3679c496ffb4', '2172797']]
        self.assertEqual(result, actual_result, "The checking of the -cid is wrong.")

    def test_multi_loc_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-cid=2172797', '-sunrise', '-city=London']
        self.assertRaisesRegex(Exception,  "Multiple chosen locations are specified.", check_command_args, commands)

    def test_dup_multi_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunrise', '-city=London']
        self.assertRaisesRegex(Exception,  "Multiple chosen locations are specified.", check_command_args, commands)

    def test_no_commands(self):
        commands = []
        self.assertRaisesRegex(Exception,  "Enter in some commands to get data from a location or use the -help command.", check_command_args, commands)

    def test_no_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-sunset=time' ]
        self.assertRaisesRegex(Exception,
                               "Only the commands -api, -city, -cid, -gc, -z and -temp allows inputs.",
                               check_command_args, commands)

    def test_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city']
        self.assertRaisesRegex(Exception,
                               "Please enter an input using a '=' after the command.\nEg. -city=London",
                               check_command_args, commands)

    def test_invalid_inputs_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-what']
        self.assertRaisesRegex(Exception,
                               "Commands aren't spelled correctly.",
                               check_command_args, commands)







if __name__ == "__main__":
    unittest.main()
