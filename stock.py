import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

metrics = ['Name', 'Exchange', 'Industry', 'PERatio', 'PEGRatio', 'BookValue', 'DividendPerShare', 'EPS', 'PriceToBookRatio']

def get_stock_info(ticker):
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=FP8AP4JBR6LP9SWU'
    json_data = requests.get(url).json()
    for metric in metrics:
        print(metric + ':', json_data[metric])