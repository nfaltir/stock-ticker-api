import requests
import pandas as pd
import json

url = "https://stock-tickers-api.herokuapp.com/get-tickers/technology"  # fix link
data = requests.get(url)


stock_sectors = pd.read_json(open('tickers/sectors.json'))


def jprint(data):
    # create a formatted string of the Python JSON object
    text = json.dumps(data, sort_keys=True, indent=4)
    print(text.replace("", ':'))


jprint(data.json())

# print(resp,"\n")
# print(resp.content)
