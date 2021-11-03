import requests

url = "https://stock-tickers-api.herokuapp.com/get-tickers/technology" #fix link
resp = requests.get(url)

print(resp,"\n")
print(resp.content)