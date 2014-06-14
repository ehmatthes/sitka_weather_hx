import requests
from time import strftime

# Define output file, and make sure it starts out blank.
output_file = "sitka_weather_history.csv"
output_file = "sitka_weather_history_2014.csv"

# Comment this out to pick up where it left off:
#with open(output_file, 'w') as myfile:
#    myfile.write('')


start_year = 1949
end_year = 2013

# test data:
#end_year = 1950

# The script is running into connection issues after long runs.
#  Need to be able to pick up where it left off.
start_year = 2013


def get_url(year, month):
    return "http://www.wunderground.com/history/airport/PASI/%d/%d/%d/MonthlyHistory.html?format=1" % (year, month, 1)


year = start_year
while year <= end_year:

    if year == start_year:
        month = 1
    else:
        month = 1

    while month <= 12:

        # Print a timestamp, to monitor a script running overnight.
        # For monitoring progress, print current month, year.
        timestamp = strftime("%m/%d/%Y %H:%M:%S")
        message = "Processing month: %d/%d" % (month, year)
        print("\n%s --- %s" % (timestamp, message))

        url = get_url(year, month)
        r = requests.get(url)

        print("                        Status code: %d" % r.status_code)

        lines = r.text.split("\n")
        with open(output_file, 'a') as myfile:
            for index, line in enumerate(lines):
                if index == 0:
                    continue
                if index == 1 and (year != start_year or month != 1):
                    continue
                line = line.replace('<br />', '') + '\n'
                #print("line: ", line)
                myfile.write(line)

        month += 1

    year += 1
