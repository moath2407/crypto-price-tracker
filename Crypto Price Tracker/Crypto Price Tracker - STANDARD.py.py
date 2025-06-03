import requests
import json
import time

def notify(message, interval):
    while True:
        print(message)
        time.sleep(interval)

def check_price_of_coin(identifier, timer, interval=None):
    baseurl = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'YOUR_API_KEY_HERE',  # Replace with your API key
    }

    response = requests.get(baseurl, headers=headers)
    print("Response Code:", response.status_code)

    data = response.json()

    found = False
    for coin in data['data']:
        if coin['symbol'] == identifier:
            price = coin['quote']['USD']['price']
            last_updated = coin['quote']['USD']['last_updated']
            message = f"As of {last_updated}, the price of {identifier} is ${round(price, 2)}"

            if timer == "Yes":
                notify(message, interval)
            else:
                print(message)
            found = True
            break

    if not found:
        print("Coin not found!")

# --- Input Section ---
identifier = input("Enter your coin symbol (BTC, ETH, etc.): ").upper()
timer = input("Would you like continuous notifications? (Yes/No): ")

interval = None
if timer == "Yes":
    interval = int(input("Notify every how many seconds?: "))

check_price_of_coin(identifier, timer, interval)
