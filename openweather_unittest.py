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
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-temp=fahrenheit']
        result = check_command_args(commands)
        # ???
        actual_result = [False, [True, False, False, False], [False, True, False, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -temp command with the input of fahrenheit is wrong.")

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

        self.assertRaisesRegex(IndexError, "-help command can only be called alone. ", check_command_args, commands)

    def test_check_input_check_with_one_input(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time']
        result = check_command_args(commands)

        actual_result = [False, [True, False, False, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the data commands is wrong.")

    def test_check_input_check_with_more_than_one_input(self):
        commands = ['openweather.py', '-pressure', '-api=170dae04cac7827d30fd3679c496ffb4', '-sunset', '-city=London', '-time']
        result = check_command_args(commands)

        actual_result = [False, [True, False, False, False], [True, False, True, True, False, False, False, True, False],
         ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the data commands is wrong.")

    def test_check_input_check_with_no_input(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London']

        self.assertRaisesRegex(IndexError, "Enter in some data commands or call the -help command.", check_command_args, commands)


if __name__ == "__main__":
    unittest.main()
