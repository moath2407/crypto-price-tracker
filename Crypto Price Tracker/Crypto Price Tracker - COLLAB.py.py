import requests
import json
from pprint import pprint as pp
from IPython.display import Javascript, display
import time

#Function to show browser alert in Google Colab
def notify(message, time1):
    display(Javascript(f'alert({json.dumps(message)})'))
    time.sleep(int(time1))
    notify(message, time1)

def check_price_of_coin(indentifier, timer, time):

  #Get the response object
  response = requests.get(baseurl, headers = headers)
  print(response.status_code)

  #Declare the dataset
  data = response.json()

  #EXAMPLE: Make it look pretty, THIS IS THE INFORMATION ABOUT BITCOIN
  #print(pp(response.json()['data'][0]['quote']))

  check_if_found = False

  for coin in data['data']:
    if coin['symbol'] == identifier:
      #Price of Identifier (LATEST)
      pricings = coin['quote']['USD']['price']
      #Time of CHECK
      time = coin['quote']['USD']['last_updated']

      if timer == "Yes":
        message = f"As of {time}, the price of {identifier} is ${round(pricings, 2)}"
        notify(message, time1)

      else:
        print("As of ", time, " , ", identifier, " costs ", pricings, " $")
      check_if_found = True
      break

  if check_if_found == False:
    print("Coin is not found.!")

baseurl = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
}

identifier = input("Enter your coin symbol (BTC, ETH, etc.)")
identifier = identifier.upper()
timer = input("Would you like to implement a notification system (Yes/No)?")

if timer == "Yes":
  time1 = int(input("How many seconds?"))
check_price_of_coin(identifier, timer, time1)