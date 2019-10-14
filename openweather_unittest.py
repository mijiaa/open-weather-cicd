from openweather import *
import unittest


class openWeatherTests(unittest.TestCase):
    def test_time_command(self):
        commands = ['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time']
        result = check_command_args(['openweather.py', '-api=170dae04cac7827d30fd3679c496ffb4', '-city=London', '-time'])

        actual_result = [False, [True, False, False, False], [True, False, True, False, False, False, False, False, False], ['170dae04cac7827d30fd3679c496ffb4', 'London']]
        self.assertEqual(result, actual_result, "The checking of the -time is wrong.")


if __name__ == "__main__":
    unittest.main()
