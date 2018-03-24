
import pandas as pd
import datetime
import numpy as np

df = pd.read_csv('budget_data_1.csv', parse_dates=['Date'])

print(df[:3])
print(df['Date'])

print(list(df))
print(df.iloc[1],[1])

dateparse = lambda x: pd.datetime.strptime(x, '%b-%y')

df = pd.read_csv('budget_data_1.csv', parse_dates=['Date'], date_parser=dateparse)

print(df)

input1 = input("Continue")

nummonths = pd.to_numeric(df.drop_duplicates('Date').count())

print(nummonths)

df = df.sort_values('Date')
rev1 = df.iloc[0,1]
print(rev1)
df = df.sort_values('Date', ascending=False)
rev2 = df.iloc[0,1]
print(rev2)
totalrev = rev2 - rev1
print(totalrev)

averagerev = totalrev / nummonths

print(averagerev)
