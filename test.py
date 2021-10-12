import requests

url = "https://stock-tickers-api.herokuapp.com/sectors"
resp = requests.get(url)

print(resp,"\n")
print(resp.content)