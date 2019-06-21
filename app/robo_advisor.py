#53:27 youtube walkthrough

import csv
import json
import datetime 
import os

import requests

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#Information Output

requests_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo"
response = requests.get(requests_url)

print(type(response))
print(response.status_code)
#print(response.text)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) 
latest_day = dates[0]


latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices) # max of all high
recent_low = min(low_prices)


#Information Output

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    #looping
    writer.writerow({
        "timestamp": "TODO",
        "open": "TODO",
        "high": "TODO",
        "low": "TODO",
        "close": "TODO",
        "volume": "TODO",
    })
    
    writer.writerow({
        "timestamp": "TODO",
        "open": "TODO",
        "high": "TODO",
        "low": "TODO",
        "close": "TODO",
        "volume": "TODO",
    })

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"Writing Data to CSV: {csv_file_path}..")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------") 

