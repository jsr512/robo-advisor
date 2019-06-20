#32 min youtube walkthrough

import requests
import json
import datetime 

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

for target_list in dates:
    high_price = tsd[latest_day]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices) # max of all high


#Information Output

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------") 