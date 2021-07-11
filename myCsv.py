import csv
import matplotlib.pyplot as plt
import datetime as dt

filename = 'myCsvData.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headline = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = dt.datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(figsize=(10, 6), dpi=128)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
plt.title("Daily high and low temperature, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
