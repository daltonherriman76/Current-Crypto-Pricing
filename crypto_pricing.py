import requests
import json

r = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR")

data = r.json()

bitcoin = data['BTC']
ethereum = data['ETH']
#print(r.status_code)
#print(bitcoin)
#print(ethereum)

print("Current Bitcoin(BTC) pricing in USD: $" + str(bitcoin['USD']))
print("Current Bitcoin(BTC) pricing in EUR: €" + str(bitcoin['EUR']))
print("Current Ethereum(ETH) pricing in USD: $" + str(ethereum['USD']))
print("Current Bitcoin(ETH) pricing in EUR: €" + str(ethereum['EUR']))
