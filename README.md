Sitka Weather History
===

Originally, a simple program to pull historical weather data for the Sitka area, and compile it into a single csv file.

Now that we have a full 60+ year data set, I can't help but play with it. So the project will probably grow to include some analysis of the data set as well.

Data Files
---

Data comes from [Weather Underground](http://www.wunderground.com/), from the section on [Sitka weather history](http://www.wunderground.com/history/airport/PASI/1949/1/25/MonthlyHistory.html?format=1). That's the text-based output for scraping; there is a gui explorer for the data [here](http://www.wunderground.com/history/airport/PASI/1949/1/25/MonthlyHistory.html).

- [Data file directory](https://github.com/ehmatthes/sitka_weather_hx/tree/master/data_files)

- [Data file with blank lines](https://raw.githubusercontent.com/ehmatthes/sitka_weather_hx/master/data_files/sitka_wx_hx_blank_lines.csv) between every month, good for visually skimming the data.

- [Data file with no blank lines](https://raw.githubusercontent.com/ehmatthes/sitka_weather_hx/master/data_files/sitka_wx_hx_no_blank_lines.csv), for a little easier work when analyzing data.