#53:27 youtube walkthrough

import csv
import json
import datetime 
import os

from dotenv import load_dotenv
import requests

load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

now = datetime.datetime.now()

#Information Input

api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")

while True: 
    symbol = input("Please enter a valid ticker symbol (example: AMZN): ")

    if len(symbol) > 4:
        print("Ticker is not valid. Please reneter")
        next 
    elif (symbol.isdigit()) == True: ##used this reference to kick out #'s https://www.geeksforgeeks.org/python-string-isdigit-application/
        print("Tickers cannot contain numbers. Please reneter")
        next 
    else:
        break
 
#Information Output

requests_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}"
response = requests.get(requests_url)

if (response.status_code) == 200:
    print("Ticker validating... printing data")
    pass
else:
    print("Oops, looks like there was a problem connecting while looking up that ticker. Please check to see the information input is correct and try again.")
    quit()

parsed_response = json.loads(response.text)

while True: # Used this reference here: https://docs.python.org/3/tutorial/errors.html
    try:
        last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
        break
    except KeyError:
        print("Oops. Looks like there was a problem with that ticker. Please check that the ticker exists and was entered properly")
        quit()

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

recent_high = max(high_prices) 
recent_low = min(low_prices)

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() 
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
        })

#Reccomendation

adjusted_high = .8 *(float(recent_high))

while True:
    if float(latest_close) >= float(adjusted_high):
        recommendation = "Sell!"
        reason = "Stock is within 20 percent of its recent high and might be overvalued."
        break

    else:  
        recommendation = "Buy!"
        reason = "Stock is 20 percent lower than its recent high and might be undervalued."
        break

#Print Statement

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print(f"REQUEST AT: {now}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {recommendation}")
print(f"RECOMMENDATION REASON: {reason}")
print("-------------------------")
print(f"Writing Data to CSV: {csv_file_path}..")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------") 

