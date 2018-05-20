# Imports
import requests
import json

# cryptocompare get request
r = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR")

# Save API response as json
data = r.json()

# Bitcoin directory returned from cryptocompare API as Python dictionary
bitcoin = data['BTC']
# Ethereum directory returned from cryptocompare API as Python dictionary
ethereum = data['ETH']

# Console outputs for Bitcoin and Ethereum in both USD and EUR, accessed 
# by indexing dictionaries at key value: 'USD' or 'EUR'
print("Current Bitcoin(BTC) pricing in USD: $" + str(bitcoin['USD']))
print("Current Bitcoin(BTC) pricing in EUR: €" + str(bitcoin['EUR']))
print("Current Ethereum(ETH) pricing in USD: $" + str(ethereum['USD']))
print("Current Bitcoin(ETH) pricing in EUR: €" + str(ethereum['EUR']))
