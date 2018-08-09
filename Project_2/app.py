import pandas as pd
import json
from urllib.request import urlopen
import time
data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=A&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

A = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

AAPL = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AMD&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

AMD = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=ARQL&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

ARQL = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AU&apikey=YJ3CRQVJ9S99JIMV'))
data = requests.get(url).json()
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

AU= my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BHP&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

BHP = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BLIN&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

BLIN = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BOSC&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

BOSC = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BP&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

BP = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BTI&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

BTI = my_data

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=INX&apikey=YJ3CRQVJ9S99JIMV'
data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IXIC&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

IXIC = my_data

data = json.load(urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=INX&apikey=YJ3CRQVJ9S99JIMV'))
data = data['Time Series (Daily)']
dates = list(data.keys())
my_data = []

for i in range(0, len(dates)):
    date = dates[i]
    my_data.append(data[date]['4. close'])
    if i < 1:
        beginning = my_data[0]
    my_data[i] = float(my_data[i]) / float(beginning)

INX = my_data

from plotly.offline import plot
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='kc.speshk', api_key='GTj6xkjbxv2JYM5QhzMz')


# Create random data with numpy
import numpy as np

# Create a trace
trace0 = go.Scatter(
    x = dates,
    y = A,
    mode = 'lines',
    name = 'A'
)
trace1 = go.Scatter(
    x = dates,
    y = AAPL,
    mode = 'lines',
    name = 'AAPL'
)
trace2 = go.Scatter(
    x = dates,
    y = AMD,
    mode = 'lines',
    name = 'AMD'
)
trace3 = go.Scatter(
    x = dates,
    y = ARQL,
    mode = 'lines',
    name = 'ARQL'
)
trace4 = go.Scatter(
    x = dates,
    y = AU,
    mode = 'lines',
    name = 'AU'
)
trace5 = go.Scatter(
    x = dates,
    y = BHP,
    mode = 'lines',
    name = 'BHP'
)
trace6 = go.Scatter(
    x = dates,
    y = BLIN,
    mode = 'lines',
    name = 'BLIN'
)
trace7 = go.Scatter(
    x = dates,
    y = BOSC,
    mode = 'lines',
    name = 'BOSC'
)
trace8 = go.Scatter(
    x = dates,
    y = BP,
    mode = 'lines',
    name = 'BP'
)
trace9 = go.Scatter(
    x = dates,
    y = BTI,
    mode = 'lines',
    name = 'BTI'
)
trace10 = go.Scatter(
    x = dates,
    y = INX,
    mode = 'lines',
    name = 'INX'
)
trace11 = go.Scatter(
    x = dates,
    y = IXIC,
    mode = 'lines',
    name = 'IXIC'
)

data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11]

py.iplot(data, filename='basic-line')
