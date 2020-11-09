import requests
from bs4 import BeautifulSoup

metrics = ['Name', 'Exchange', 'Industry', 'PERatio', 'PEGRatio', 'BookValue', 'DividendPerShare', 'EPS', 'PriceToBookRatio']

def get_stock_info(ticker):
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=Putyourapikeyhere'
    json_data = requests.get(url).json()
    for metric in metrics:
        print(metric + ':', json_data[metric])
