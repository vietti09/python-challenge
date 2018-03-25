
import pandas as pd
import datetime
import numpy as np

df = pd.read_csv('budget_data_1.csv', parse_dates=['Date'])

dateparse = lambda x: pd.datetime.strptime(x, '%b-%y')

df = pd.read_csv('budget_data_1.csv', parse_dates=['Date'], date_parser=dateparse)

nummonths = pd.to_numeric(df.drop_duplicates('Date').count()).iloc[0]

f= open("budget.txt","w")

print("\n Financial Analysis \n ",\
    "------------------- \n")
f.write("Financial Analysis \n ------------------- \n")

print("Total Number of Months:     " + str(nummonths))
f.write("Total Number of Months:     ")
f.write(str(nummonths))

df = df.sort_values('Date')
rev1 = df.iloc[0,1]
print("\n Initial Revenue: $" + str(rev1))
f.write("\n Initial Revenue: $")
f.write(str(rev1))

df = df.sort_values('Date', ascending=False)
rev2 = df.iloc[0,1]

print("\n Ending Revenue: $" + str(rev2))
f.write("\n Ending Revenue: $")
f.write(str(rev2))

totalrev = rev2 - rev1
print("\n Total Revenue: $" + str(totalrev))
f.write("\n Total Revenue: $")
f.write(str(totalrev))

averagerev = totalrev / nummonths

print("\n Average Revenue Per Month: $" + str(round(averagerev,2)))
f.write("\n Average Revenue Per Month: $")
f.write(str(round(averagerev,2)))

series1 = df.Revenue.max()

print("\n Greatest Increase in Revenue: $" + str(series1))
f.write("\n Greatest Increase in Revenue: $")
f.write(str(series1))

series2 = df.Revenue.min()
print("\n Greatest Decrease in Revenue: $" + str(series2))
f.write("\n Greatest Decrease in Revenue: $")
f.write(str(series2))

print("\n Have A Nice Day XOXO")
f.close()