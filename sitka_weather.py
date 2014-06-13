import requests

output_file = "sitka_weather_history.csv"
with open(output_file, 'w') as myfile:
    myfile.write('')

url = "http://www.wunderground.com/history/airport/PASI/1949/1/25/MonthlyHistory.html?format=1"

r = requests.get(url)

print(r.status_code)

lines = r.text.split("\n")
with open(output_file, 'a') as myfile:
    for line in lines:
        line = line.replace('<br />', '')
        print("line: ", line)
        myfile.write(line)
