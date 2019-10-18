# project
Name : openweather.py
Description : This is a Weather Forecast program. We implemented a command-line program in Python 3+
to get weather forecast through the OpenWeatherMap API. Below are descriptions on how to use the program.

1)This program can accept 14 command-line arguments to return the current weather data which are,
-api=API token
-city=city name
-cid=city id
-gc=geographic coordinates
-z=zip code
-time
-temp=( celsius , fahrenheit) (the default unit is celsius)
-pressure
-cloud
-humidity
-wind
-sunset
-sunrise
-help

2)This program can accept more than one option at a time. Given a valid option and input, this program will
return a message based on the chosen information.
Example:
python openweather.py -api=XXX -city="London" -temp="celsius"
- This command line will produce a string - "The temperature ranges from 10.08-11.98 celsius."

3)Please note that there should not be any spaces between command-line arguments and data input.
example :
-city="London" (correct)
-city=London (correct)
-city = "London" (incorrect)

4)Please also take note that there is only one dash for command-line arguments
example:
-city="London" (correct)
--city="London" (incorrect)

5)The position of command-lines arguments are flexible (-city can come before -api and vice versa)
but take note that there should not be any duplication of command line arguments
examples:
python openweather.py -api=XXX -city="London" -temp="celsius" (correct)
python openweather.py -city="London" -temp="celsius"-api=XXX (correct))
python openweather.py -city="London" -temp="celsius"-api=XXX -temp="fahrenheit" (incorrect))


6)"-help" can only be called alone
example:
python openweather.py -help (correct)
python openweather.py -help -api=XXX -city="London" (incorrect)
FIT2107 project repository

7) "-wind" command can give either only the wind speed or the wind speed plus the angle of the wind depending on weather
the forecast gave the information

8) -city, -cid, -gc, -z are called location commands in our program.information

9) -time, -temp, -pressure, -cloud, -humidity, -wind, -sunset, -sunrise are called data commands in our program