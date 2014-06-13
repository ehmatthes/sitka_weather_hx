import requests

# Define output file, and make sure it starts out blank.
output_file = "sitka_weather_history.csv"
with open(output_file, 'w') as myfile:
    myfile.write('')

start_year = 1949
start_month = 1
day = 1

end_year = 2014
end_month = 5

# test data:
end_year = 1950
end_month = 3

def get_url(year, month):
    return "http://www.wunderground.com/history/airport/PASI/%d/%d/%d/MonthlyHistory.html?format=1" % (year, month, 1)


year = start_year
month = start_month

while year <= end_year:

    while month <= end_month:

        print("Processing month: %d/%d" % (month, year))
        url = get_url(year, month)
        r = requests.get(url)

        print("Status code: %d" % r.status_code)

        lines = r.text.split("\n")
        with open(output_file, 'a') as myfile:
            for index, line in enumerate(lines):
                if index == 0:
                    continue
                if index == 1 and (year != start_year or month != start_month):
                    continue
                line = line.replace('<br />', '') + '\n'
                #print("line: ", line)
                myfile.write(line)

        month += 1

    year += 1
