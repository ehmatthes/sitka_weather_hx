import csv

# A script to run some simple initial analysis on the data:
#
# - Pull the data into Python data structures.
# - Create simple graphs of the numerical data.
# - Create some monthly totals/ averages, and annual totals/ averages.
# - Plot some of these monthly/ annual results.
#
# - Make it easier to answer more interesting questions about
#     long-term patterns and historical anomalies.


# Data file to work with.
filename = 'data_files/sitka_wx_hx_no_blank_lines.csv'
filename = 'data_files/sitka_wx_hx_no_blank_lines_2014.csv'

daily_highs = []
with open(filename) as f:
    reader = csv.reader(f)

    next(reader)

    for row in reader:
        daily_highs.append(int(row[1]))

print('daily highs:', daily_highs[0:5])
print('len:', len(daily_highs))
